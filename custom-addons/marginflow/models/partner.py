from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    marginflow_note = fields.Char(
        string="MarginFlow Note",
    )
