from odoo import models, fields, api, _


class ResPartner(models.Model):

    _inherit = "res.partner"

    absence_ids = fields.One2many(
        'absences',
        'student_id',
        string='Absences'
    )
    absence_count = fields.Integer(
        string='Number of absence',
        compute='_compute_absence_count',
        store=True
    )
# method for counting the number of absences

    @api.depends('absence_ids')
    def _compute_absence_count(self):
        for partner in self:
            partner.absence_count = self.env['absences'].search_count([
                ('student_id', '=', partner.id)
            ])

    def action_view_absences(self):
        self.ensure_one()
        return {
            'name': 'Absences',
            'type': 'ir.actions.act_window',
            'res_model': 'absences',
            'view_mode': 'tree,form',
            'domain': [('student_id', '=', self.id)],
            'context': {
                'default_student_id': self.id,
                'search_default_student_id': self.id
            },
        }
