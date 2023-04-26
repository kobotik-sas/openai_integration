# -*- coding: utf-8 -*-
{
    'name': 'OpenAI Integration',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integrate OpenAI API with Odoo',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'license': 'AGPL-3',
    'depends': [
        # Add any Odoo module dependencies here
    ],
    'external_dependencies': {
        'python': ['requests'],
    },
    'data': [
        'views/openai_config_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
