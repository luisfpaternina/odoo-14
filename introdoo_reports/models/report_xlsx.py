# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging


class ReportXlsx(models.AbstractModel):
    _name = 'report.introdoo_reports.report_customer_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, sale):
        for line in sale.order_line:
            format1 = workbook.add_format({'font_size': 13, 'align': 'vcenter', 'bold': True})
            format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
            sheet = workbook.add_worksheet('Hoja canal Introdoo')
            sheet.write(2, 2, 'Contactos', format1)
            sheet.write(2, 3, line.name, format2)
