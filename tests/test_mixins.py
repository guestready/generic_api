import mock
from django.test import TestCase

from generic_api import mixins
from generic_api.tests.generics.generic_objects import (TestGetEndpoint,
                                                        TestPostEndpoint)


class RequestValidationMixinTestCase(TestCase):
    def setUp(self):
        self.mixin = mixins.RequestValidationMixin()

    def test_get_request_entity_class(self):
        self.assertIsNone(self.mixin.get_request_entity_class())

    def test_get_request_entity_context(self):
        self.assertEqual(self.mixin.get_request_entity_context(), {})

    def test_get_request_entity(self):
        self.assertIsNone(self.mixin.get_request_entity())

    def test_validate_request(self):
        self.assertEqual(self.mixin.validate_request(None), None)


class ResponseValidationMixinTestCase(TestCase):
    def setUp(self):
        self.mixin = mixins.ResponseValidationMixin()

    def test_get_response_entity_class(self):
        self.assertIsNone(self.mixin.get_response_entity_class())

    def test_get_response_entity_context(self):
        self.assertEqual(self.mixin.get_response_entity_context(), {})

    def test_get_response_entity(self):
        self.assertIsNone(self.mixin.get_response_entity())

    def test_validate_response(self):
        self.assertEqual(self.mixin.validate_response(None), None)


class GetRequestMixinTestCase(TestCase):
    def setUp(self):
        self.endpoint = TestGetEndpoint()

    @mock.patch('generic_api.generics.client.requests.get')
    def test_get_request(self, mock_get):
        self.endpoint.get_request()
        self.assertTrue(mock_get.called)


class PostRequestMixinTestCase(TestCase):
    def setUp(self):
        self.endpoint = TestPostEndpoint()

    @mock.patch('generic_api.generics.client.requests.post')
    def test_post_request(self, mock_post):
        self.endpoint.post_request()
        self.assertTrue(mock_post.called)
