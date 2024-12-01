from odoo import models, fields, api, _


class Absences(models.Model):

    _name = 'absences'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_class_id = fields.Many2one(
        string="class", comodel_name="school.class")

    parents_student_id = fields.Many2one(
        comodel_name = 'res.partner',
        domain= "[('role_id.name', '=', 'student_id'),('role_id.name', '=', 'Parent')]"
    )

    student_id = fields.Many2one(
        'res.partner',
        string='Student',
        required=True,
        domain="[('class_id', '=', student_class_id), ('role_id.name', '=', 'Student')]")

    teacher_who_noted_absence_id = fields.Many2one(
        string='teacher who noted absence',
        comodel_name='res.partner',
        domain="[('role_id.name', '=', 'Teacher')]")
    
    absence_type_id = fields.Many2one(
        comodel_name='absence.type',
        string='Absence Type',
    )

    day_of_absence = fields.Datetime(string='day of absence',
                                     default=fields.Datetime.now
                                     )

    time_of_absence = fields.Selection(
        string='Time of Absence',
        selection=[
            ('morning', 'Morning'),
            ('afternoon', 'Afternoon')
        ],
        required=True,
        compute='_compute_time_of_absence',
        readonly=False
    )

    rel_is_justified = fields.Boolean(
        string='Is Justified',
        related='absence_type_id.is_justify',
        readonly=True,
        store=True,
        help="Indicates if the absence is justified"
    )

    absence_count = fields.Integer(
        string='Number of absences',
        compute='_compute_absence_count',
        store=True
    )
    is_confirm = fields.Boolean(string="confirm by parents")

    @api.depends('day_of_absence')
    def _compute_time_of_absence(self):
        for record in self:
            if record.day_of_absence:
                hour = record.day_of_absence.hour
                if hour < 12:
                    record.time_of_absence = 'morning'
                else:
                    record.time_of_absence = 'afternoon'

    def action_send_mail_to_parents(self):

        mail_template = self.env.ref('school_diary.parents_mail')

        ctx = {
            'default_model': 'absences',
            'default_res_ids': self.ids,  # Fetches the model's ids
            'default_template_id': mail_template.id,
        }

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'target': 'new',
            'context': ctx,
        }
