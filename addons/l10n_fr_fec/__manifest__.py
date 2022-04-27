#-*- coding:utf-8 -*-
# Part of midrarsolutions. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2013-2015 Akretion (http://www.akretion.com)

{
    'name': 'France - FEC Export',
    'icon': '/l10n_fr/static/description/icon.png',
    'category': 'Accounting/Localizations/Reporting',
    'summary': "Fichier d'Échange Informatisé (FEC) for France",
    'author': "Akretion,midrarsolutions Community Association (OCA)",
    'depends': ['l10n_fr', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/account_fr_fec_view.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
