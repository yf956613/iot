from odoo import models
import os
import logging
_logger = logging.getLogger(__name__)
try:
    import pika
except (ImportError, IOError) as err:
    _logger.debug(err)


class IoTSystemAction(models.Model):
    _inherit = 'iot.system.action'

    def _run(self, device_action):
        if self != self.env.ref('iot_amqp.amqp_action'):
            return super()._run(device_action)
        url = self.env['ir.config_parameter'].sudo().get_param(
            'amqp.host'
        )
        connection = pika.BlockingConnection(pika.URLParameters(url))
        channel = connection.channel()
        result = channel.basic_publish(
            device_action.output_id.amqp_exchange,
            device_action.output_id.amqp_routing_key,
            device_action.output_id.amqp_payload,
        )
        _logger.info(result)
        connection.close()
