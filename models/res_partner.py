from odoo import models, fields 

class ResPartner(models.Model): 
    _inherit = "res.partner"
    
    booking_ids = fields.One2many(
        
        "kayak.booking" , 
        "partner_id" , 
        string = "Historial de reservas ")