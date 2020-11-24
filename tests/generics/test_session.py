from django.test import TestCase

from .generic_objects import TestSession


class GenericRetriesHandlerTestCase(TestCase):
    def setUp(self):
        self.session = TestSession()

    def test_headers(self):
        self.assertEqual(self.session.headers(), {})

    def test_params(self):
        self.assertEqual(self.session.params(), {})

    def test_get_base_url(self):
        self.assertEqual(self.session.get_base_url(), 'https://www.example.com/')
