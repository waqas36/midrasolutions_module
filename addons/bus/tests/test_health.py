# Part of midrarsolutions. See LICENSE file for full copyright and licensing details.

from odoo.tests import HttpCase


class TestBusController(HttpCase):
    def test_health(self):
        response = self.url_open('/longpolling/health')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['status'], 'pass')
        self.assertNotIn('session_id', response.cookies)
