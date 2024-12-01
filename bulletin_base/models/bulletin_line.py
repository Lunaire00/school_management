# -*- coding: utf-8 -*-

from odoo import models, fields, _ ,api
from odoo.exceptions import ValidationError


class BulletinLine(models.Model):
    _name = 'bulletin.line'
    _description = 'Bulletin line Model'

    bulletin_id = fields.Many2one('bulletin',string="Note")  ## link back to One2Many
    student_id = fields.Many2one(related='bulletin_id.student_id', string="Student",store=True)  ## not sure it's needed
    course_id=fields.Many2one('school.course',string="Course")
    grade = fields.Integer(string="Grade")

    teacher_id = fields.Many2one(related='course_id.teacher_id', string='Teacher', store=True)
    number_of_hours = fields.Integer(related='course_id.hours', store=True)
    average_score = fields.Integer(compute='_compute_average_score', string='Average score')

    @api.onchange('grade')
    def _compute_average_score(self):
        for rec in self:
            grades = self.env['bulletin.line'].search([('student_id', '=', rec.student_id.id)]).mapped('grade')
            if len(grades) != 0:
                rec.average_score = sum(grades) / len(grades)
            else:
                rec.average_score = 0

    @api.constrains('grade')
    def _check_grade_value(self):
        for rec in self:
            if  rec.grade < 0 or rec.grade > 100:
                msg = f"Error : Grade must be between 0 and 100\n{rec.grade} was entered"
                raise ValidationError(_(msg))
