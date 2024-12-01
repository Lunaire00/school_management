# -*- coding: utf-8 -*-
from odoo import models, fields, _


class CommentType(models.Model):
    _name = 'comment.type'
    _description = "comment.type"

    name = fields.Char(string=_("Name of comment"))
    gravity_level = fields.Integer(string="gravity Level")
