# -*- coding: utf-8 -*-
# Part of midrarsolutions. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    siret = fields.Char(string='SIRET', size=14)

