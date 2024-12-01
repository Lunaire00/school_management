# -*- coding: utf-8 -*-
{
    'name': "school_management_base",

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
    'depends': ['base', 'account','mail', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/school_base_role_data.xml',
        'views/school_management_base_menus.xml',
        'views/school_base_role_views.xml',
        'views/res_partner_views.xml',
        'views/partner_view.xml',
        'views/school_course_views.xml',
        'views/school_base_degre_config_views.xml',
        'views/school_base_course_config_views.xml',
        'views/school_class_views.xml',
        'views/school_course_category_views.xml',
        'views/school_base_program_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'data/res_partner_demo.xml',
        'data/school_base_degre_config_demo.xml',
        'data/school_base_course_config_demo.xml',
        'data/course_demo.xml',
        'data/program_demo.xml',
    ],
}

