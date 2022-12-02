from odoo import fields, models, api, _
from datetime import datetime

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'
