# -*- coding: utf-8 -*-
from odoo import models, fields, _


class AbsenceType(models.Model):
    _name = 'absence.type'
    _description = "absence.type"
        
    name = fields.Char(string=_("Type of absence"))
    is_justify = fields.Boolean(string=_("Justify"))

    