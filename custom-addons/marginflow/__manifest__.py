{
    "name": "MarginFlow",
    "version": "1.0",
    "summary": "Simple quotation margin module",
    "description": """
MarginFlow
==========

Simple quotation and margin management module.
""",
    "category": "Sales",
    "author": "Samuel",
    "license": "LGPL-3",

    "depends": [
        "base",
    ],

    "data": [
        "security/ir.model.access.csv",
        "views/quotation_views.xml",
    ],

    "installable": True,
    "application": True,
    "auto_install": False,
}
