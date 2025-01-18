from odoo import fields, models


class ResCompanyType(models.Model):
    _name = "res.company.type"

    name = fields.Char()

    type = fields.Char()
