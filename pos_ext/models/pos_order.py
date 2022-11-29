from odoo import fields, models, api, _
from datetime import datetime

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    tax_ids = fields.Many2many(
        'account.tax',
        string="Taxes")

    def action_done_show_wizard(self):
       return {'type': 'ir.actions.act_window',
               'name': _('Update taxes'),
               'res_model': 'pos.order.line.wizard',
               'target': 'new',
               'view_id': self.env.ref('pos_ext.pos_order_line_wizard').id,
               'view_mode': 'form',
               'context': {'default_order_id': self.order_id.id}
               }
