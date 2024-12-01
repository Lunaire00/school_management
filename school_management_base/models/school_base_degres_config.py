from odoo import api, fields, models, _


class SchoolBaseDegreConfig(models.Model):
    _name = 'school.base.degre.config'
    _description="school.base.degre.config"
    
    name = fields.Char(string=_("name"))
    academy_level = fields.Selection(selection=[('secondary', 'Secondary'), ('primary', 'Primary')], default='secondary')