# Copyright (C) 2018 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class IoTSystem(models.Model):
    _name = 'iot.system'
    _description = 'IoT System'

    name = fields.Char(required=True)
    output_ids = fields.One2many('iot.device.output', inverse_name='system_id')
    system_action_ids = fields.One2many(
        'iot.system.action', inverse_name='system_id'
    )
