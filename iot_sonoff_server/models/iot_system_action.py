import logging
from odoo import models
import requests

_logger = logging.getLogger(__name__)


class IoTSystemAction(models.Model):
    _inherit = 'iot.system.action'

    def _run_sonoff_server(self, device_action, action=False):
        params = {
            'ip': device_action.device_id.ip,
        }
        if action:
            params['action'] = action,
        request = requests.get(
            self.env['ir.config_parameter'].sudo().get_param(
                'iot.sonoff.server'
            ), params=params
        )
        request.raise_for_status()
        return request.text

    def _run(self, device_action):
        if self == self.env.ref(
            'iot_sonoff_server.iot_sonoff_server_action_on'
        ):
            return self._run_sonoff_server(device_action, 'on')
        if self == self.env.ref(
            'iot_sonoff_server.iot_sonoff_server_action_off'
        ):
            return self._run_sonoff_server(device_action, 'off')
        if self == self.env.ref(
            'iot_sonoff_server.iot_sonoff_server_action_status'
        ):
            return self._run_sonoff_server(device_action)
        return super()._run(device_action)
