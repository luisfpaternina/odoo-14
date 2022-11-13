# -*- coding: utf-8 -*-
#BY: LUIS FELIPE PATERNINA VITAL
from odoo import models, fields,_
from odoo.exceptions import ValidationError


class Students(models.Model):

    _name = "students"
    _inherit = 'mail.thread'
    _description = "students"

    name = fields.Char(string='Name', required=True, tracking=True)
    identification_type = fields.Selection([('cc','CC'),('ni','NI'),('ce','CE')], string="ID Type", tracking=True)
    identification_number = fields.Char(string="Identification Number", tracking=True)
    photo = fields.Binary(string='Photo', tracking=True)
    dob = fields.Date(string="Date of Birth", tracking=True)
    gender = fields.Selection([('m', 'Male'), ('f', 'Female'), ('o', 'Otro')], string='Gender')
    blood_group = fields.Selection(
        [('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'),
         ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB-', 'AB-')],
        string='Blood Group')
    nationality = fields.Many2one('res.country', string='Nacionality')
    city_id = fields.Many2one('res.city', string="City")
    attachment = fields.Binary(string="Attachment", tracking=True)
    address = fields.Char(string="Address")
    cellphone = fields.Char(string="Phone")
    neighborhood = fields.Char(string="Neighborhood")
    email = fields.Char(string="Email")

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s - %s'%(rec.identification_number, rec.name)))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('identification_number', operator, name)]
        result self._search(domain + args, limit=limit, acess_rights_uid=name_get_uid)


    _sql_constraints = [

    ('name_unique',
     'UNIQUE(identification_number)',
     "The identification number must be unique!")

    ]
