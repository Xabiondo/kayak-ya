from odoo import models , fields

class ResService(models.Model):
    _name = "res.service"
    _description = "servicio de alquiler de Kayak" 

    name = fields.Char(string ="nombre del servicio" , required = True)
    description = fields.Text(string = "Descripción ")
    price = fields.Float(string = "precio por hora" , required = True)
    duration = fields.Float(string = "Duración Estándar(Horas)" , required = True)
    active = fields.Boolean(string = "Activo" , default = True)

