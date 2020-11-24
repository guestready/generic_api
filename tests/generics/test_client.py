import mock
from django.test import TestCase

from .generic_objects import (TestClient, TestErrorsHandler,
                              TestRetriesHandler, TestSession)


class ClientTestCase(TestCase):
    def setUp(self):
        self.client = TestClient()

    def test_get_session_class(self):
        session_class = self.client.get_session_class()
        self.assertEqual(session_class, TestSession)

    def test_get_session_context(self):
        context = self.client.get_session_context()
        self.assertEqual(context, {})

    def test_get_session(self):
        session = self.client.get_session()
        self.assertEqual(session.__class__, TestSession)

    def test_get_errors_handler_class(self):
        errors_handler_class = self.client.get_errors_handler_class()
        self.assertEqual(errors_handler_class, TestErrorsHandler)

    def test_get_errors_handler_context(self):
        context = self.client.get_errors_handler_context()
        self.assertEqual(context, {})

    def test_get_errors_handler(self):
        errors_handler = self.client.get_errors_handler()
        self.assertEqual(errors_handler.__class__, TestErrorsHandler)

    def test_get_retries_handler_class(self):
        retries_handler_class = self.client.get_retries_handler_class()
        self.assertEqual(retries_handler_class, TestRetriesHandler)

    def test_get_retries_handler_context(self):
        context = self.client.get_retries_handler_context()
        self.assertEqual(context, {})

    def test_get_retries_handler(self):
        retries_handler = self.client.get_retries_handler()
        self.assertEqual(retries_handler.__class__, TestRetriesHandler)

    def test_get_base_url(self):
        self.assertEqual('https://www.example.com/', self.client.get_base_url())

    def test_request(self):
        request_method = mock.Mock()
        self.client._request(request_method, 'https://www.example_target.com/', data={})
        self.assertTrue(request_method.called)

    @mock.patch('generic_api.generics.client.requests.get')
    def test_get(self, mock_get):
        self.client.get('https://www.example_target.com/')
        self.assertTrue(mock_get.called)

    @mock.patch('generic_api.generics.client.requests.post')
    def test_post(self, mock_post):
        self.client.post('https://www.example_target.com/', data={})
        self.assertTrue(mock_post.called)
