from odoo import api, fields, models, _

class SchoolBaseProgram(models.Model):
    _name = 'school.base.program'
    _description = "school.base.program"
    
    name = fields.Char(string=_("Name"))
    cours_ids = fields.Many2many(comodel_name="school.course", string=_("Course"))
    degre_ids = fields.Many2one(comodel_name="school.base.degre.config", string=_("Degre"))
    total_hours = fields.Integer(string="Total hours", compute="_compute_total_hours", readonly=True)
    cours_ids_domain = fields.Binary(string="Course Domain", compute="_compute_cours_ids_domain")
    student_ids = fields.One2many(comodel_name="res.partner", inverse_name="option", string="Students")

    @api.depends('cours_ids')
    def _compute_total_hours(self):
        for rec in self:
            hours_sum = rec.cours_ids.mapped('hours')
            rec.total_hours = sum(hours_sum)

    @api.depends('degre_ids')
    def _compute_cours_ids_domain(self):
        for rec in self:
            if rec.degre_ids:
                rec.cours_ids_domain = [('degree_id', '=', rec.degre_ids.name)]
            else:
                rec.cours_ids_domain = []


