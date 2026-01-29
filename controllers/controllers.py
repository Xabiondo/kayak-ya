

from odoo import http
from odoo.http import request

class KayakController(http.Controller):
    @http.route('/api/kayak/bookings' , type='json' , auth='user')

    # Así protegemos las rutas efectivamente 

    def get_bookings(self):
        bookings = request.env['res.booking'].search_read(
            [] , 
            ['name' , 'start_date' , 'state']

        )
        return {'status' : 'success' , 'data' : bookings}
