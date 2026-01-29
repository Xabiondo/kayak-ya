from odoo import models, fields 

class ResPartner(models.Model): 
    _inherit = "res.partner"

    is_vip = fields.Boolean(string = "Es cliente VIP , tiene 10% descuento" , default = False)
    
    booking_ids = fields.One2many(
        
        "res.booking" , 
        "partner_id" , 
        string = "Historial de reservas ")