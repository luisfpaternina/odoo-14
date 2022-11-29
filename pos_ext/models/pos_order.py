from odoo import fields, models, api
from datetime import datetime

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    tax_ids = fields.Many2many(
        'account.tax',
        string="Taxes")

    def update_taxes(self):
        ids = []
        for record in self:
            if not record.tax_ids_after_fiscal_position:
                ids.append(record.tax_ids.ids)
                record.write({'tax_ids_after_fiscal_position': [(6, 0 , ids)]})
