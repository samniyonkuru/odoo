from odoo import fields, models


class MarginFlowQuotation(models.Model):
    _name = "marginflow.quotation"
    _description = "MarginFlow Quotation"

    name = fields.Char(string="Quotation", required=True)
    customer = fields.Char(string="Customer")
    sales_price = fields.Float(string="Sales Price")
    cost = fields.Float(string="Cost")
