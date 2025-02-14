{
    "name": "Russia - Documents",
    "version": "11.0.0.0.1",
    "author": "CodUP, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-russia",
    "license": "AGPL-3",
    "category": "Localization",
    "depends": ["sale_management"],
    "external_dependencies": {
        "python": ["pytils"],
    },
    "demo": ["demo/l10n_ru_doc_demo.xml"],
    "data": [
        "views/account_invoice_view.xml",
        "views/res_partner_view.xml",
        "views/res_company_view.xml",
        "views/res_users_view.xml",
        "views/res_bank_view.xml",
        "data/l10n_ru_doc_data.xml",
        "reports/l10n_ru_doc_report.xml",
        "reports/report_order.xml",
        "reports/report_invoice.xml",
        "reports/report_bill.xml",
        "reports/report_act.xml",
        "data/bill_action_data.xml",
    ],
    "css": ["static/src/css/l10n_ru_doc.css"],
    "installable": True,
}
