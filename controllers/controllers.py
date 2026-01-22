

from odoo import http
from odoo.http import request

class KayakController(http.Controller):
    @http.route('/api/kayak/bookings' , type='json' , auth='public')

    #Este método es inseguro , una persona sin autenticar puede descargarse la base de datos, tenemos que darle una vuelta equipo. 
    def get_bookings(self):
        bookings = request.env['kayak.booking'].sudo().search_read([] , ['name' , 'start_date' , 'state'])
        return {'status': 'success', 'data': bookings}
