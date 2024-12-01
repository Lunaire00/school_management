# -*- coding: utf-8 -*-

from odoo import models, fields, _


class AcademicYear(models.Model):
    _name = 'academic.year'
    _description = 'Academic Year Model'

    name = fields.Char(string=_("Name"), required=True)
    start_date = fields.Date(string=_("Start Date"), required=True)
    end_date = fields.Date(string=_("End Date"), required=True)
    period_ids = fields.One2many('period', 'year_id', string='Periods')