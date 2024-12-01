from odoo import fields, models

class SchoolBaseRole(models.Model):
    _name = "school.base.role"
    _description = "School Base Role"

    name = fields.Char(string="Name", required=True)
