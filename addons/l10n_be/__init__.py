# -*- coding: utf-8 -*-
# Part of midrarsolutions. See LICENSE file for full copyright and licensing details.

from odoo import api, SUPERUSER_ID

from . import models

def load_translations(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env.ref('l10n_be.l10nbe_chart_template').process_coa_translations()
