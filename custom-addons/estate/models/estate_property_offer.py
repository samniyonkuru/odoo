from dateutil.relativedelta import relativedelta
from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Property Offer"

    name = fields.Char(string="Name")

    price = fields.Float()

    status = fields.Selection(
            [
                ("accepted", "Accepted"),
                ("refused", "Refused"),
                ],
            copy =False,
            )

    partner_id = fields.Many2one(
            "res.partner",
            required=True,
            )

    property_id = fields.Many2one(
            "estate.property",
            required=True,
            )

    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)


    validity = fields.Integer(default=7)

    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("validity")
    def _compute_date_deadline(self):
        for rec in self:
            rec.date_deadline = fields.Date.today() + relativedelta(days=rec.validity)

    def _inverse_date_deadline(self):
        for rec in self:
            rec.validity = (rec.date_deadline - fields.Date.today()).days
