# -*- coding: utf-8 -*-

from openerp import api, models, fields, _

'''
This module create model of Course
'''

class Course(models.Model):
    '''
    This class create model of Course
    '''
    _name = 'openacademy.course' # Model odoo name

    name = fields.Char(string='Title', required=True) # Field reserved to identified name rec
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null',
                                     string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    new_field = fields.Char('My New Field', help="My new help")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         _("The title of the course should not be the description")),

        ('name_unique',
         'UNIQUE(name)',
         _("The course title must be unique")),
    ]

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', _(u"Copy of {}%").format(self.name))])
        if not copied_count:
            new_name = _(u"Copy of {}").format(self.name)
        else:
            new_name = _(u"Copy of {} ({})").format(self.name, copied_count)

        default['name'] = new_name
        default['test_1'] = _('Test 1')
        default['test_2'] = _('Test 2')
        default['test_3'] = _('Test 3')
        default['test_4'] = _('Test 4')
        default['test_5'] = _('Test 5')
        default['test_8'] = _('Test 8')
        default['test_9'] = _('Test 9')
        default['test_10'] = _('Test 10')
        default['test_11'] = _('Test 11')
        default['test_12'] = _('Test 12')
        default['test_13'] = _('Test 13')
        default['test_14'] = _('Test 14')
        default['test_15'] = _('Test 15')
        default['test_16'] = _('Test 16')
        default['test_17'] = _('Test 17')
        default['test_18'] = _('Test 18')
        default['test_19'] = _('Test 19')
        default['test_20'] = _('Test 23')
        default['test_20'] = _('Test 24')
        default['test_20'] = _('Test 25')
        default['test_20'] = _('Test 26')
        default['test_20'] = _('Test 27')
        default['test_20'] = _('Test 28')
        default['test_20'] = _('Test 29')
        default['test_20'] = _('Test 30')
        default['test_20'] = _('Test 31')
        default['test_20'] = _('Test 32')
        default['test_20'] = _('Test 33')
        default['test_20'] = _('Test 34')
        default['test_20'] = _('Test 35')
        default['test_20'] = _('Test 36')
        default['test_20'] = _('Test 37')
        default['test_20'] = _('Test 38')
        return super(Course, self).copy(default)

