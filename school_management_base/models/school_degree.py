from odoo import models, fields

class SchoolCourse(models.Model):
    _name = 'school.degree'
    _description = 'Degree'

    name = fields.Char(string='Degree', required=True)
