# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolManagementBase(http.Controller):
#     @http.route('/school_management_base/school_management_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_management_base/school_management_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_management_base.listing', {
#             'root': '/school_management_base/school_management_base',
#             'objects': http.request.env['school_management_base.school_management_base'].search([]),
#         })

#     @http.route('/school_management_base/school_management_base/objects/<model("school_management_base.school_management_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_management_base.object', {
#             'object': obj
#         })

