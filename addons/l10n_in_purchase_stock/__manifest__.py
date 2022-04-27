# -*- coding: utf-8 -*-
# Part of midrarsolutions. See LICENSE file for full copyright and licensing details.

{
    'name': "India Purchase and Warehouse Management",
    'icon': '/l10n_in/static/description/icon.png',

    'summary': """
        Define default purchase journal on the warehouse""",

    'description': """
        Define default purchase journal on the warehouse,
        help you to choose correct purchase journal on the purchase order when
        you change the picking operation.
        useful when you setup the multiple GSTIN units.
    """,

    'author': "midrarsolutions",
    'website': "https://www.midrarsolutions.app",
    'category': 'Accounting/Localizations/Purchase',
    'version': '1.0',

    'depends': ['l10n_in_purchase', 'l10n_in_stock'],

    'data': [
        'views/stock_warehouse_views.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
