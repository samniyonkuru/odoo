from odoo import models, fields


class RealEstate(models.Model):
    _name = "estate.property"
    _description = "Real estate Model"

    active = fields.Boolean(default=True, invisible=True)
    name = fields.Char(required=True)
    state = fields.Selection(
            [
                ("new", "New"),
                ("received", "Offer Received"),
                ("accepted", "Offer Accepted"),
                ("sold", "Sold"),
                ("canceled","Canceled"),
                ],
            required=True,
            copy=False,
            default="new"
            )

    postcode = fields.Char()
    
    def default_date(self):
        return fields.Date.today()

    date_availability = fields.Date(default= default_date)
    expected_price = fields.Float(required=True)
    best_offer = fields.Float()
    selling_price = fields.Float()
    
    description = fields.Text()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west", "West"),
    ])

    property_type_id = fields.Many2one(
            "estate.property.type",
            string="Property Type",
            )

    buyer_id = fields.Many2one(
            "res.partner",
            string="Buyer",
            copy=False,
            )

    salesperson_id = fields.Many2one(
            "res.users",
            string="Salesperson",
            default=lambda self: self.env.user,
            )
