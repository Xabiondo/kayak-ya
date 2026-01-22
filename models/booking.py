from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime , timedelta

class KayakBooking(models.Model):
    _name="kayak.booking"
    _descripcion="Reserva de Kayak"
    _inherit=["mail.thread","mail.activity.mixin"] 

    name= fields.Char(string="Referencia", required=True, copy=False, readonly=True, default="Nuevo")
    partner_id= fields.Many2one("res.partner",string="Cliente", required=True)
    service_id= fields.Many2one("kayak.service",string="Servicio", required=True)
    start_date= fields.Datetime(string="Fecha Inicio", required=True)
    end_date= fields.Datetime(string="Fecha Fin", compute="_compute_end_date", store=True)
    state= fields.Selection([("draft","Borrador"),("confirmed", "Confirmado"),("invoiced","Facturado"),("cancelled","Cancelado")], default="draft", string="Estado", tracking=True)

    invoice_id= fields.Many2one("account.move", string="Factura Vinculada", readonly=True)

    @api.depends("start_date", "service_id.duration")
    def _compute_end_date(self):
        for record in self:
            if record.start_date and record.service_id:
                record.end_date= record.start_date + timedelta(hours = record.service_id.duration)
            else:
                record.end_date = record.start_date

    @api.constrains("start_date")
    def _check_dates(self):
        for record in self:
            if record.start_date < fields.Datetime.now():
                raise ValidationError("Fecha no valida.")

    def action_confirm(self):
        self.state="confirmed"
        self._create_invoice()

    def _create_invoice(self):
        invoice_vals={"move_type":"out_invoice", "partner_id":self.partner_id.id,
            "invoice_line_ids": [(0,0,{"name":self.service_id.name,"quantity":1,"price_unit":self.service_id.price})]}
        invoice=self.env["account.move"].create(invoice_vals)
        self.invoice_id=invoice.id
        self.state="invoiced"
