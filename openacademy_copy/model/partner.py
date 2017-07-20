# -*- coding: utf-8 -*-
from openerp import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    instructor_copy = fields.Boolean("Instructor Copy", default=False)


