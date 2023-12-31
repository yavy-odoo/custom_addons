# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Motorcycle Registry",
    "version": "1",
    "category": "Kawiil/Kawiil",
    'icon': '/motorcycle_registry/static/img/icon.png',
    "summary": "Manage Registration of Motorcycles",
    "description": """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    "author": "yavy-odoo",
    "website": "https://github.com/yavy-odoo/",
    "depends": [
        "base",
        "stock",
        "website"
    ],
    "data": [
        "security/motorcycle_groups.xml",
        "security/ir.model.access.csv",
        "views/motorcycle_menuitems.xml",
        "views/registry_views.xml",
        "views/product_template_view_inherit.xml",
        "views/motorcycle_web_templates.xml",
    ],
    "demo": [
        "demo/motorcycle_demo.xml",
    ],
    # "assets": [],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True
}
