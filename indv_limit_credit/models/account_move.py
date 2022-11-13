# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    has_credit = fields.Boolean(
        string="Has a current credit",
        related="partner_id.has_credit")
    credit_value = fields.Float(
        string="Credit value",
        related="partner_id.credit_value")


    @api.constrains('partner_id')
    def _check_has_credit(self):
        for record in self:
            if record.has_credit and record.amount_total > record.credit_value:
                raise ValidationError(_("Cannot make this sale because the amount exceeds the customer's credit limit: %s" % record.credit_value))
