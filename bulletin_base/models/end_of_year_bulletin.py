# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class YearEndBulletin(models.Model):
    _name = 'end.bulletin'
    _description = 'Bulletin for End of Year Model'

    name = fields.Char(string=_("Bulletin Name"),default="Test") #, readonly=True, compute="_compute_name", default="")
    # bulletin_date = fields.Date(string=_("Bulletin Date"))
    # student_id = fields.Many2one('res.partner', string=_("Student"), required=True, domain="[('role_type', '=', 'student')]")  # , domain="[('role_type', '=', 'student')]"
    # student_image = fields.Binary(related='student_id.image_1920')

    # class_id = fields.Char(string=_("Class"),related='student_id.class.name')                    #needs class field in res.partner Model
    # main_teacher_id =fields.Char(string=_('Main Teacher'),related='class_id.teacher_id.name')    #needs teacher_id field in class Model

    # note_ids = fields.One2many('bulletin.note', 'bulletin_id', string=_("Notes"))
    # year_id = fields.Many2one('academic.year', string=_("Year"), default="")  ## needs to be created by group1 instead ?
    # period_id = fields.Many2one('period', string=_("Period"), default="")
    # type = fields.Selection(selection=[('formation', _('Formation')), ('period', _('Period')), ('exam', _('Exam'))])

    bulletin_ids = fields.One2many('bulletin','end_of_year_bulletin_id',string="Bulletins")