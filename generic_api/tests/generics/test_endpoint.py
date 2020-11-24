import mock
from django.test import TestCase

from .generic_objects import (TestClient, TestGenericEndpoint, TestGetEndpoint,
                              TestPostEndpoint)


class GenericEndpointTestCase(TestCase):
    def setUp(self):
        self.endpoint = TestGenericEndpoint()

    def test_get_endpoint_url(self):
        self.assertEqual('https://www.example_endpoint.com/', self.endpoint.get_endpoint_url())

    def test_get_client_class(self):
        self.assertEqual(TestClient, self.endpoint.get_client_class())

    def test_get_client_context(self):
        self.assertEqual({}, self.endpoint.get_client_context())

    def test_get_client(self):
        self.assertEqual(self.endpoint.get_client().__class__, TestClient)


class GetEndpointTestCase(TestCase):
    def setUp(self):
        self.endpoint = TestGetEndpoint()

    def test_get(self):
        with mock.patch('generic_api.generics.client.requests.get') as mock_get:
            mock_get.return_value = mock.Mock()
            self.endpoint.get()
            self.assertTrue(mock_get)

    def test_post(self):
        with self.assertRaises(AttributeError):
            self.endpoint.post()


class PostEndpointTestCase(TestCase):
    def setUp(self):
        self.endpoint = TestPostEndpoint()

    def test_get(self):
        with self.assertRaises(AttributeError):
            self.endpoint.get()

    def test_post(self):
        with mock.patch('generic_api.generics.client.requests.post') as mock_post:
            mock_post.return_value = mock.Mock()
            self.endpoint.post()
            self.assertTrue(mock_post)
