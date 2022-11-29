from odoo import fields, models, api
from datetime import datetime

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    tax_ids = fields.Many2many(
        'account.tax',
        string="Taxes")
