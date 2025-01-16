from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _commercial_fields(self):
        return super(__class__, self)._commercial_fields() + ["kpp"]

    kpp = fields.Char(string="KPP", help="Tax Registration Reason Code")
