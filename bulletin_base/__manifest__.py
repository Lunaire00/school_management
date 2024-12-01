# -*- coding: utf-8 -*-
{
    'name': "Manage Bulletins",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Jonathan, Bertin, Arthur",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'assets': {
        'web.assets_backend': [
            'bulletin_base/static/src/css/custom_styles.css',
        ],
    },


    # any module necessary for this one to work correctly
    'depends': ['base','school_management_base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bulletin_views.xml',
        'views/academic_year_views.xml',
        'views/period_views.xml',
        'views/res_partner_views.xml',
        'views/end_of_year_bulletin_views.xml',
        'data/academic_year_example.xml',
        'data/period_example.xml',
        # 'data/bullettin_data.xml',
        'report/report_period_bulletin.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    
    'installable':True,
    'application':True,

}

