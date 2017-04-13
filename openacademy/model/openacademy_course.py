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
        default['test_6'] = _('Test 6')
        default['test_7'] = _('Test 7')
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
        default['test_20'] = _('Test 20')
        default['test_20'] = _('Test 21')
        default['test_20'] = _('Test 22')
        default['test_20'] = _('Test 23')
        return super(Course, self).copy(default)

