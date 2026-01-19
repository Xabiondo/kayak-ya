

from odoo import http
from odoo.http import request

class KayakController(http.Controller):
    @http.route('/api/kayak/bookings' , type='json' , auth='public')
    def get_bookings(self):
        bookings = request.env['kayak.booking'].sudo().search_read([] , ['name' , 'start_date' , 'state'])
        return {'status': 'success', 'data': bookings}
