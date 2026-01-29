from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta

class Booking(models.Model):
    _name = 'res.booking'
    _description = 'Reserva de Servicios'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Referencia", required=True, copy=False, readonly=True, default=lambda self: _('Nuevo'))
    

    partner_id = fields.Many2one('res.partner', string="Cliente", required=True)
    service_id = fields.Many2one('res.service', string="Servicio", required=True, domain="[('active', '=', True)]")

    start_date = fields.Datetime(string="Fecha Inicio", required=True)
    end_date = fields.Datetime(string="Fecha Fin", compute="_compute_end_date", store=True)
    

    price_total = fields.Float(string="Precio Total", compute="_compute_price", store=True)
    invoice_id = fields.Many2one('account.move', string="Factura", readonly=True)

    state = fields.Selection([
        ('draft', 'Pendiente'),
        ('confirmed', 'Confirmado'),
        ('invoiced', 'Facturado'),
        ('cancelled', 'Cancelado')
    ], default='draft', string="Estado", tracking=True)


    @api.depends('start_date', 'service_id.duration')
    def _compute_end_date(self):
        for record in self:
            if record.start_date and record.service_id:
                record.end_date = record.start_date + timedelta(hours=record.service_id.duration)
            else:
                record.end_date = False


    @api.depends('service_id', 'partner_id.is_vip')
    def _compute_price(self):
        for record in self:
            if record.service_id:
                base_price = record.service_id.price * record.service_id.duration
                if record.partner_id.is_vip:
                    record.price_total = base_price * 0.90  # 10% descuento
                else:
                    record.price_total = base_price
            else:
                record.price_total = 0.0


    @api.constrains('start_date', 'service_id')
    def _check_constraints(self):
        for record in self:
            if record.start_date < fields.Datetime.now():
                raise ValidationError("No puedes reservar en el pasado.")
            

            overlap = self.search_count([
                ('id', '!=', record.id),
                ('service_id', '=', record.service_id.id),
                ('state', 'in', ['confirmed', 'invoiced']),
                ('start_date', '<', record.end_date),
                ('end_date', '>', record.start_date)
            ])
            if overlap > 0:
                raise ValidationError("Ya existe una reserva confirmada para este servicio en ese horario.")


    def action_confirm(self):
        self._create_invoice()
        self.state = 'confirmed'

    def _create_invoice(self):
        invoice_vals = {
            'move_type': 'out_invoice',
            'partner_id': self.partner_id.id,
            'invoice_line_ids': [(0, 0, {
                'name': f"Reserva: {self.service_id.name}",
                'quantity': 1,
                'price_unit': self.price_total, 
            })]
        }
        invoice = self.env['account.move'].create(invoice_vals)
        self.invoice_id = invoice.id

    @api.model
    def _check_expired_bookings(self):
     
        limit_time = fields.Datetime.now() - timedelta(hours=24)

        expired = self.search([('state', '=', 'draft'), ('create_date', '<', limit_time)])
        for doc in expired:
            doc.state = 'cancelled'