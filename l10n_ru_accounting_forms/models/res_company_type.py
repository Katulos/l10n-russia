from odoo import fields, models


class ResCompanyType(models.Model):
    _name = "res.company.type"
    _description = "Russian Company Types"

    name = fields.Char()

    type = fields.Char()
