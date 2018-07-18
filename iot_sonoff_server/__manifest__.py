# Copyright (C) 2017 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'IoT Sonoff Server',
    'version': '11.0.1.0.0',
    'category': 'IoT',
    'author': "Creu Blanca, "
              "Odoo Community Association (OCA)",
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'summary': 'IoT base',
    'depends': [
        'iot',
    ],
    'data': [
        'data/config_data.xml',
        'data/iot_system_data.xml',
        'views/iot_device_views.xml',
    ],
}
