from odoo import fields, models, api, _
from datetime import datetime
import logging


class WizardPosOrderLine(models.TransientModel):
    _name = "pos.order.line.wizard"
    _description = "Pos order line wizard"

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
        line = self.env['pos.order.line'].search([('id', '=', self.line_id.id)], limit=1)
        for record in self:
            if record.line_id:
                line.write({'tax_ids_after_fiscal_position': record.tax_ids.ids})
                logging.info('*******************************************************')
