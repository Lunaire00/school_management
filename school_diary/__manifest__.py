# -*- coding: utf-8 -*-
{
    'name': "school_diary",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','school_management_base'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/absence_type_data.xml",
        "data/comment_type_data.xml",
        "data/period_week_type_data.xml",
        "data/parents_mail.xml",
        "data/comment_mail.xml",
        #"data/comment_data.xml",
        "data/absences_data.xml",
        "views/views.xml",
        "views/templates.xml",
        "views/absences_views.xml",
        "views/absences_type_views.xml",
        "views/comment_type_views.xml",
        "views/period_week_type_views.xml",
        "views/school_diary_menu_views.xml",
        "views/res_partner_views.xml",
        "report/comment_report.xml",
        "views/comment_views.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

