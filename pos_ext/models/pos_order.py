from odoo import fields, models, api
from datetime import datetime

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'
