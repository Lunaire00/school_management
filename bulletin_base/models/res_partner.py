# coding: utf-8
from odoo import models, fields, _


class Partner(models.Model):
    _inherit = 'res.partner'

    bulletin_ids = fields.One2many('bulletin', 'student_id', string=_("Bulletins"))

    def action_res_bulletin_button(self):

        return {'type': 'ir.actions.act_window',
                'name': 'Action Smart',
                'res_model': 'bulletin',
                'target': 'self',
                'view_mode': 'tree,form',
                'view_type': 'tree',
                'domain':[('id', 'in', self.bulletin_ids.ids)],
                # 'context': {'default_customer_name': self.owner_id.id}
                }
