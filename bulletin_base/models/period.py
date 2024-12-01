# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Period(models.Model):
    _name = 'period'
    _description = 'Period of the year and their weight'

    name = fields.Char(string=_('Period Name'), required=True)
    beginning_date = fields.Date(string=_('Start Period'), required=True)
    ending_date = fields.Date(string=_('End Period'), required=True)
    period_weight = fields.Integer(string=_('Percentage'), required=True, default=0)
    is_certif = fields.Boolean(string=_('Certif'))
    year_id = fields.Many2one('academic.year', string='Academic Year', required=True)
    
    # _sql_constraints = [('name_uniq', "unique(name)", _('Period name already existe'))]

    @api.onchange('is_certif', 'period_weight')
    def _check_certif(self):
        '''
        If period is not a certification period, the period weight
        is automatically set to zero
        '''
        if self.is_certif == False:
            self.period_weight = 0


    @api.constrains('name')
    def _check_name(self):
        '''
        Check that a period cannot have the same name. 
        Note that a period in another year can have the same name.
        '''
        for rec in self:
            periods_name = self.env['period'].search([('year_id', '=', rec.year_id.id)]).sorted('id').mapped('name')
        periods_name.pop()
        if self.name in periods_name:
            raise ValidationError(_(f"Period name : {self.name} already existe for this year"))

    @api.constrains('beginning_date', 'ending_date')
    def _check_period_date(self):
        '''
        Verify that a new period is not going to overlaps a precedent one
        '''
        start_dates = self.env['period'].search([]).sorted('id').mapped('beginning_date')
        ending_dates = self.env['period'].search([]).sorted('id').mapped('ending_date')
        start_dates.pop()
        ending_dates.pop()
        
        for start, end in zip(start_dates, ending_dates):
            if (start <= self.beginning_date <= end):
                raise ValidationError(_(f"Error : {self.beginning_date} is inside another period"))
            elif start <= self.ending_date <= end:
                raise ValidationError(_(f"Error : {self.ending_date} is inside another period"))
            elif self.beginning_date < start and self.ending_date > end:
                raise ValidationError(_(f"Error : {self.beginning_date} - {self.ending_date} include another period"))
            else:
                continue

    @api.constrains('period_weight')
    def _check_period_weight(self):
        '''
        Check that the period weight is set between 0 and 100 inclusive and that the total 
        amout of period weights is not higher than 100  
        '''
        if 0 <= self.period_weight >= 100:
            raise ValidationError(_(f'Error : Period weight must be between 0 and 100'))
        for rec in self:
            periods = self.env['period'].search([('year_id', '=', rec.year_id.id)]).mapped('period_weight')
        if sum(periods) > 100:
            raise ValidationError(_(f'Error : Period weight exceeds 100.00\n{100 - sum(periods) + self.period_weight}% is available'))

    @api.constrains('beginning_date', 'ending_date')
    def _check_year_includes_period(self):
        '''
        Check that the year selected includes the dates of the period 
        '''
        start_year = self.year_id.start_date
        end_year = self.year_id.end_date
        if not (self.beginning_date >= start_year and self.ending_date <= end_year):
            raise ValidationError(_(f"Period {self.name} is not included in {self.year_id.name}\nAcademic Year start: {self.year_id.start_date}\nAcademic Year end: {self.year_id.end_date}"))
