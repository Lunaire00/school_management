# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolDiary(http.Controller):
#     @http.route('/school_diary/school_diary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_diary/school_diary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_diary.listing', {
#             'root': '/school_diary/school_diary',
#             'objects': http.request.env['school_diary.school_diary'].search([]),
#         })

#     @http.route('/school_diary/school_diary/objects/<model("school_diary.school_diary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_diary.object', {
#             'object': obj
#         })

