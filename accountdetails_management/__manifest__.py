# -*- coding: utf-8 -*-
# Part of Odoo, Flectra. See LICENSE file for full copyright and licensing details.
{
    'name':" My Account Details Management App",
    'author': 'Shakir',
    'installable': True,
    'auto_install': False,
    'version' : '1.1',
    'summary': 'My Account Details',
    'depends' : ['base'],
    'data': ['views/account_details_view.xml',
             'views/bank_name_view.xml',
             'views/account_holder_view.xml'],
    'demo': [],
    'category':'Hidden',
    'description':'TEST'
}