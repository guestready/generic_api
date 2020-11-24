import mock
from django.test import TestCase

from generic_api.session import ConstanceSession


class TestConstanceSession(ConstanceSession):
    base_url = 'https://www.example_constance_session.com/'
    constance_key = 'test_session'


class ConstanceSessionTestCase(TestCase):
    def setUp(self):
        self.session = TestConstanceSession()

    def test_headers(self):
        self.assertEqual(self.session.headers(), {})

    def test_params(self):
        with mock.patch('generic_api.session.config') as mock_config:
            mock_config.test_session = 'bearer AAA'
            self.assertEqual(self.session.params(), {'access_token': 'bearer AAA'})
