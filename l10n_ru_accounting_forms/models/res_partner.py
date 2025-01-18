from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    kpp = fields.Char(
        string="KPP",
        help="Reason code for registration.",
        tracking=True,
        size=9,
    )

    company_l10n_ru_type = fields.Many2one("res.company.type", string="Company Type")
