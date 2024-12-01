# -*- coding: utf-8 -*-

from odoo import models, fields, api, _, Command


class Bulletin(models.Model):
    _name = 'bulletin'
    _description = 'Bulletin Model'

    name = fields.Char(string=_("Bulletin Name"), readonly=True, compute="_compute_name", default="")
    bulletin_date = fields.Date(string=_("Bulletin Date")) #not shown yet in view
    student_id = fields.Many2one('res.partner', string=_("Student"), required=True,domain="[('role_type', '=', 'student')]")
    student_image = fields.Binary(related='student_id.image_1920',string="")

    class_id = fields.Char(related='student_id.student_class_id.name', string=_("Class")  )
    # main_teacher_id =fields.Char(string=_('Main Teacher'),related='class_id.teacher_id.name')    #needs teacher_id field in class Model

    course_ids = fields.Many2many(related='student_id.course_ids', string=_("Notes"))
    line_ids=fields.One2many('bulletin.line','bulletin_id', string="Notes")
    average_note = fields.Integer(related='line_ids.average_score')

    period_id = fields.Many2one('period', string=_("Period"), default="")
    year_id = fields.Many2one(related='period_id.year_id', string=_("Year"))  ## needs to be created by group1 instead ?
    type = fields.Char(string="Type",compute="_compute_type") ## add a related

    end_of_year_bulletin_id=fields.Many2one('end.bulletin',string="End of year bulletin")

    _sql_constraints = [
        ('unique_name',
         'unique(name)',
         'You already added a bulletin for this student for this period and this year.')
    ]

    @api.depends('student_id', 'year_id', 'period_id')
    def _compute_name(self):  # computes
        for record in self:
            if not record.year_id.name:
                temp_name = "/"
            else:
                temp_name = str(record.year_id.name).replace(" ", "") + "/"

            if not record.period_id.name:
                temp_name += "/"
            else:
                temp_name += str(record.period_id.name).replace(" ", "") + "/"

            if record.student_id.name:
                temp_name += str(record.student_id.name).replace(" ", "")
            record.name = temp_name

    @api.depends('period_id')
    def _compute_type(self):
        for record in self:
            if record.period_id.is_certif:
                record.type = "Certification"
            else:
                record.type = "Formation"

    @api.model
    def write(self, vals):
        for rec in self:
            if vals.get('student_id'):
                course_ids = self.env['res.partner'].browse(
                    vals.get('student_id')).course_ids
                line_ids = list()
                for record in course_ids:
                    line = self.env['bulletin.line'].create({
                        'bulletin_id': rec.id,
                        'course_id': record.id,
                    })
                    line_ids.append(line.id)
                vals.update({
                    'line_ids': line_ids
                })
        return super().write(vals)
