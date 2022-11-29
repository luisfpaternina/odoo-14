from odoo import fields, models, api, _
from datetime import datetime

class WizardPosOrderLine(models.TransientModel):
    _name = "pos.order.line.wizard"
    _description = "Pos order lie wizard"

    order_id = fields.Many2one(
        'pos.order',
        string="Order")
    line_id = fields.Many2one(
        'pos.order.line',
        string="Line")
    tax_ids = fields.Many2many(
        'account.tax',
        string="Taxes")

    def update_taxes(self):
        ids = []
        for record in self:
            if not record.tax_ids_after_fiscal_position:
                ids.append(record.tax_ids.ids)
                record.write({'tax_ids_after_fiscal_position': [(6, 0 , ids)]})
