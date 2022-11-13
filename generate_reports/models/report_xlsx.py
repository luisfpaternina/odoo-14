# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
import logging


class ReportXlsx(models.AbstractModel):
    _name = 'report.generate_reports.report_customer_xlsx'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 13, 'align': 'vcenter', 'bold': True})
        format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
        sheet = workbook.add_worksheet('reporte lfpv')
        sheet.write(2, 2, 'Gasto', format1)
        sheet.write(2, 3, lines.name, format2)
