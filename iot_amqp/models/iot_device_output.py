from odoo import fields, models


class IotDeviceOutput(models.Model):
    _inherit = 'iot.device.output'

    amqp_exchange = fields.Char()
    amqp_routing_key = fields.Char()
    amqp_payload = fields.Char()
