# -*- coding: utf-8 -*-
# Part of midrarsolutions. See LICENSE file for full copyright and licensing details.

{
    'name': 'midrarsolutionsBot',
    'version': '1.2',
    'category': 'Productivity/Discuss',
    'summary': 'Add midrarsolutionsBot in discussions',
    'description': "",
    'website': 'https://www.midrarsolutions.app/app/discuss',
    'depends': ['mail'],
    'auto_install': True,
    'installable': True,
    'application': False,
    'data': [
        'views/res_users_views.xml',
        'data/mailbot_data.xml',
    ],
    'demo': [
        'data/mailbot_demo.xml',
    ],
    'assets': {
        'mail.assets_discuss_public': [
            'mail_bot/static/src/models/*/*.js',
        ],
        'web.assets_backend': [
            'mail_bot/static/src/models/*/*.js',
            'mail_bot/static/src/scss/odoobot_style.scss',
        ],
        'web.tests_assets': [
            'mail_bot/static/tests/**/*',
        ],
        'web.qunit_suite_tests': [
            'mail_bot/static/src/models/*/tests/*.js',
        ],
    },
    'license': 'LGPL-3',
}
