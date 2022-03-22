# -*- coding: utf-8 -*-
{
    'name': 'Odoo Basic Model',
    'summary': '''
        Odoo Basic Model Form,List
    ''',
    'author': 'Francisco castillo',
    'category': 'Installer',
    'version': '1.0',
    'depends': [
        'base',
        'hr'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/prueba_views.xml',
        'views/hr_employee_views.xml',
        ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
