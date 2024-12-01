from odoo import api, fields, models, _


class Partner(models.Model):
    _inherit = 'res.partner'

    role_id = fields.Many2one("school.base.role")
    rel_name = fields.Char(related="role_id.name")
    partner_ids = fields.Many2many("res.partner", 'res_partner_rel', 'partner_id', 'parent_partner_id', domain="[('rel_name', '=', 'Parent')]")

    # Fields for Student
    class_id = fields.Many2one(
        'school.class',
        string='Classroom',
        domain="[('id', '!=', False)]"
    )
    option = fields.Many2one(comodel_name="school.base.program", string='Option')
    course_ids = fields.Many2many('school.course', string="Courses", compute="_compute_course_ids")
    role_type = fields.Selection(string='Role Type',
        selection=[('student', 'Student'), ('teacher', 'Teacher'), ('direction', 'Direction'), ('parent', 'Parent'), ('others', 'Others')])

    @api.onchange('role_id')
    def _onchange_role_type(self):
        for record in self:
            if record.role_id == self.env.ref('school_management_base.res_partner_role_0'):
                record.role_type = 'student'
            elif record.role_id == self.env.ref('school_management_base.res_partner_role_1'):
                record.role_type = 'teacher'
            elif record.role_id == self.env.ref('school_management_base.res_partner_role_2'):
                record.role_type = 'direction'
            elif record.role_id == self.env.ref('school_management_base.res_partner_role_3'):
                record.role_type = 'parent'
            elif record.role_id == self.env.ref('school_management_base.res_partner_role_4'):
                record.role_type = 'others'
            else:
                record.role_type = None

    partner_ids = fields.Many2many("res.partner", 'res_partner_rel', 'partner_id', 'parent_partner_id', domain="[('role_type', '=', 'parent')]")

    student_class_id = fields.Many2one(
        'school.class',
        string='Classroom'
    )
    
    is_titular=fields.Boolean(string="Is Titular")

    current_class_titular_id = fields.Many2one(
        'school.class',
        string="Titular Class",
        compute='_compute_class_titular',
        store=True
    )

    current_titular_name = fields.Char(
        string="Class Titular",
        compute="_compute_titular_name",
        store=True
    )

    titular_class_ids = fields.One2many(
        'school.class',
        'titular_id',
        string= "Classes Titular"
     )

    titular_class_names = fields.Char(
        string="Classes Titular",
        compute='_compute_class_names',
        readonly=True
    )

    @api.depends('titular_class_ids')
    def _compute_class_names(self):
        for record in self:
            class_names = ', '.join(record.titular_class_ids.mapped('name'))
            record.titular_class_names = class_names

    @api.onchange('role_id')
    def onchange_role_id(self):
        for partner in self:
            partner.is_company = False
            partner.is_titular = False

    @api.depends('student_class_id.titular_id',"is_titular")
    def _compute_class_titular(self):
        for partner in self:
         if partner.role_type == 'student':
            if partner.student_class_id and partner.student_class_id.titular_id:
                partner.current_class_titular_id = partner.student_class_id.titular_id.id
            else:
                partner.current_class_titular_id = False
        else:
            partner.current_class_titular_id = False

    @api.depends('student_class_id.titular_id',"is_titular")
    def _compute_titular_name(self):
        for partner in self:
            partner.current_titular_name = (
                partner.student_class_id.titular_id.name
                if partner.student_class_id and partner.student_class_id.titular_id
                else ""
            )

    @api.depends('option')
    def _compute_course_ids(self):
        for rec in self:
            if rec.option:
                rec.course_ids = rec.option.cours_ids
            else:
                rec.course_ids = []



