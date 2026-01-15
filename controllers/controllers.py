# -*- coding: utf-8 -*-
# from odoo import http


# class Kayak-ya(http.Controller):
#     @http.route('/kayak-ya/kayak-ya', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kayak-ya/kayak-ya/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kayak-ya.listing', {
#             'root': '/kayak-ya/kayak-ya',
#             'objects': http.request.env['kayak-ya.kayak-ya'].search([]),
#         })

#     @http.route('/kayak-ya/kayak-ya/objects/<model("kayak-ya.kayak-ya"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kayak-ya.object', {
#             'object': obj
#         })

