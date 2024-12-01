from odoo import models, fields,api

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'School Class'

    name = fields.Char(string="Class Name", required=True)
    
    students = fields.One2many('res.partner', 'student_class_id', string="Students")

    titular_id= fields.Many2one(
        'res.partner',
        string='Titular',
        domain="[('role_type', '=', 'teacher'), ('is_titular', '=', True)]"
        )

    student_count = fields.Integer(
        string="Number of Students", 
        compute="_compute_student_count", 
        store=True)

    student_ids = fields.One2many(
        'res.partner', 
        'student_class_id', 
        string="Student List",
        domain="[('role_type', '=', 'student')]"
    )

    @api.depends('students')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.students)


