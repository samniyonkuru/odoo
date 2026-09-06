from odoo import api, fields, models

from ..domain.margin import MarginInput, calculate_margin


class MarginFlowQuotation(models.Model):
    _name = "marginflow.quotation"
    _description = "MarginFlow Quotation"

    name = fields.Char(string="Quotation", required=True)
    customer_id = fields.Many2one(
            "res.partner",
            string="Customer",
        )
    sales_price = fields.Float(string="Sales Price")
    material_cost = fields.Float(string="Material Cost")
    production_cost = fields.Float(string="Production Cost")
    total_cost= fields.Float(
        string="Total Cost",
        compute="_compute_margin",
        store=True,
    )
    margin = fields.Float(
        string="Margin",
        compute="_compute_margin",
        store=True,
    )
    margin_percent = fields.Float(
        string="Margin %",
        compute="_compute_margin",
        store=True,
    )

    @api.depends("sales_price", "material_cost", "production_cost")
    def _compute_margin(self):
        for record in self:
            input_data = MarginInput(
                sales_price=record.sales_price,
                material_cost=record.material_cost,
                production_cost=record.production_cost,
            )

            output = calculate_margin(input_data)

            record.total_cost= output.total_cost
            record.margin = output.margin
            record.margin_percent = output.margin_percent
