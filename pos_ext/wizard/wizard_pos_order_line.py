from odoo import fields, models, api, _
from datetime import datetime
import logging
from odoo.exceptions import ValidationError


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
        if self.order_id.state == 'draft':
            taxes = self.env['account.tax'].browse(self.tax_ids.ids)
            linea = self.line_id
            linea.write({'tax_ids': taxes})
        else:
            raise ValidationError("Los impuestos solo se pueden modificar cuando el pedido está en Nuevo")
