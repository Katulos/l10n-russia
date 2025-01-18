from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    kpp = fields.Char(
        string="KPP",
        related="partner_id.kpp",
        help="Reason code for registration.",
        tracking=True,
        size=9,
    )

    company_l10n_ru_type = fields.Many2one(
        "res.company.type", related="partner_id.company_l10n_ru_type"
    )
