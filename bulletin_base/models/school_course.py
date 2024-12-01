# coding: utf-8
from odoo import models, fields, _


class SchoolCourse(models.Model):
    _inherit = 'school.course'

    bulletin_note_ids = fields.One2many('bulletin.line', 'course_id')
