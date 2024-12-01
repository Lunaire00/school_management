# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class PeriodWeekType(models.Model):
    _name = 'period.week.type'
    _description = "period.week.type"

    week_day = fields.Selection(string=_("Week day"),
                                selection=[
        ('monday', _('Monday')),
        ('tuesday', _('Tuesday')),
        ('wednesday', _('Wednesday')),
        ('thursday', _('Thursday')),
        ('friday', _('Friday'))
    ])
    start_time = fields.Float(string=_("Start date"))
    end_time = fields.Float(string=_("End date"))
    is_rest = fields.Boolean(string=_("Rest"))
