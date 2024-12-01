# -*- coding: utf-8 -*-
# from odoo import http


# class Bulletin(http.Controller):
#     @http.route('/bulletin/bulletin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bulletin/bulletin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bulletin.listing', {
#             'root': '/bulletin/bulletin',
#             'objects': http.request.env['bulletin.bulletin'].search([]),
#         })

#     @http.route('/bulletin/bulletin/objects/<model("bulletin.bulletin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bulletin.object', {
#             'object': obj
#         })

