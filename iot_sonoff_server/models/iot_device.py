from odoo import api, fields, models


class IoTDevice(models.Model):
    _inherit = 'iot.device'

    is_sonoff_server = fields.Boolean(
        store=True, compute='_compute_is_sonoff_server')
    state = fields.Selection(selection_add=[
        ('sonoff-server-on', 'On'),
        ('sonoff-server-off', 'Off')
    ])

    @api.multi
    @api.depends('system_id')
    def _compute_is_sonoff_server(self):
        sonoff = self.env.ref('iot_sonoff_server.iot_sonoff_server_system')
        for rec in self:
            rec.is_sonoff_server = (rec.system_id == sonoff)


class IoTDeviceAction(models.Model):
    _inherit = 'iot.device.action'

    def run_extra_actions(self, status, result):
        res = super().run_extra_actions(status, result)
        sonoff_server_on = self.env.ref(
            'iot_sonoff_server.iot_sonoff_server_action_on'
        )
        sonoff_server_off = self.env.ref(
            'iot_sonoff_server.iot_sonoff_server_action_off'
        )
        if status == 'ok' and self.system_action_id == sonoff_server_on:
            self.device_id.state = 'sonoff-server-on'
        if status == 'ok' and self.system_action_id == sonoff_server_off:
            self.device_id.state = 'sonoff-server-off'
        return res
