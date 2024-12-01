from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'Cours'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string='Course Name', required=True)
    teacher_id = fields.Many2one('res.partner', string='Teacher',
                                 domain="[('role_type', '=', 'teacher')]",
                                 tracking=True)
    # parent_id = fields.Many2one('school.course', 'Parent Category', index=True, ondelete='cascade')
    image = fields.Image(related='teacher_id.image_1920', string="Image")
    # child_id = fields.One2many('school.course', 'parent_id', 'Child Categories')
    type_ids = fields.Many2many('school.base.course.config', string='Course Type')
    hours = fields.Integer(string='Number of Hours')
    degree_id = fields.Many2one('school.base.degre.config', string='Degree')
    rel_academy_level = fields.Selection(related='degree_id.academy_level')
    sequence = fields.Integer(string="sequence")


    # course_count = fields.Integer( compute='_compute_product_count',
    #     help="The number of products under this category (Does not consider the children categories)")

    # avatax_category_id = fields.Many2one(
    #     'product.avatax.category',
    #     help="https://taxcode.avatax.avalara.com/",
    # )

    @api.model
    def write(self, vals):
        if 'teacher_id' in vals:
            for record in self:
                old_teacher = record.teacher_id
                result = super(SchoolCourse, self).write(vals)
                new_teacher = record.teacher_id
                if old_teacher != new_teacher:
                    body = "Teacher %s your course has been changed" % new_teacher.name
                    record.message_post(body=body)
                return result
        else:
            return super(SchoolCourse, self).write(vals)

    # @api.constrains('parent_id')
    # def _check_category_recursion(self):
    #     if not self._check_recursion():
    #         raise ValidationError(_('You cannot create recursive categories.'))
    #
    # @api.depends_context('hierarchical_naming')
    # def _compute_display_name(self):
    #     if self.env.context.get('hierarchical_naming', True):
    #         return super()._compute_display_name()
    #     for record in self:
    #         record.display_name = record.name
    #
    # def _compute_product_count(self):
    #     for record in self:
    #         record.parent_id += 1
