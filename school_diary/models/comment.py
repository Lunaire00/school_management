from odoo import models, fields, api, _, Command


class Comment(models.Model):
    _name = "comment"
    _description = "comment on the student"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    student_class = fields.Many2one(
        string="class", comodel_name="school.class")
    
    student_id = fields.Many2one(string="student", comodel_name="res.partner", required=True,
                                 domain="[('role_type', '=', 'student')]")
    
    teacher_id = fields.Many2one(string="teacher", comodel_name="res.partner",
                                 required=True, domain="[('role_type', '=', 'teacher')]")
    
    type_comment_id = fields.Many2one(
        string="type comment", comodel_name='comment.type', required=True)
    
    rel_gravity_level = fields.Integer(related='type_comment_id.gravity_level')
    
    is_confirm = fields.Boolean(string="confirm by parents")


    def action_send_mail_comment_to_parents(self):

        mail_template = self.env.ref('school_diary.comment_mail')

        ctx = {
            'default_model': 'comment',
            'default_res_ids': self.ids,
            'default_template_id': mail_template.id,
        }

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }
