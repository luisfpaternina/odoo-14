from odoo import fields, models, api, _
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

    def action_done_show_wizard(self):
       return {'type': 'ir.actions.act_window',
               'name': _('Add taxes'),
               'res_model': 'pos.order.line.wizard',
               'target': 'new',
               'view_id': self.env.ref('pos_ext.pos_order_line_wizard').id,
               'view_mode': 'form',
               'context': {}
               }
