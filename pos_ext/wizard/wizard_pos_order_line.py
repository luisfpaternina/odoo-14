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
        pedido = env['pos.order'].browse(self.order_id)
        logging.info('--------------------------------------')
        logging.info(pedido)
        iva = env['account.tax'].browse(19)
        linea = pedido.lines[7]
        linea.write({'tax_ids':iva})
