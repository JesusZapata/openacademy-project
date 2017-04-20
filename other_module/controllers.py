# -*- coding: utf-8 -*-
from openerp import http

# class OtherModule(http.Controller):
#     @http.route('/other_module/other_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/other_module/other_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('other_module.listing', {
#             'root': '/other_module/other_module',
#             'objects': http.request.env['other_module.other_module'].search([]),
#         })

#     @http.route('/other_module/other_module/objects/<model("other_module.other_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('other_module.object', {
#             'object': obj
#         })