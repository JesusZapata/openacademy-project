# -*- coding: utf-8 -*-

from openerp import models, fields, _


class test_module(models.Model):
    _name = 'test_module.test_module'
    name = fields.Char()

    def method(self):
        _("Test")
        _("Test 2")
