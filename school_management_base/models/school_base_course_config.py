from odoo import api, fields, models, _


class SchoolBaseCourseConfig(models.Model):
    _name = 'school.base.course.config'
    _description="school.base.course.config"
    
    name = fields.Char(string=_("name"))
    color = fields.Integer(string=_("Color"))