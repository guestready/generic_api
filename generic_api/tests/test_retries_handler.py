from django.test import TestCase
from requests.models import Response

from generic_api.retries_handler import RetryOnError


class TestRetryOnError(RetryOnError):
    error_codes = [503]
    retry_count = 2


class RetryOnErrorTestCase(TestCase):
    def setUp(self):
        self.retries_handler = TestRetryOnError()

    def test_is_eligible_false_due_to_error_code(self):
        response = Response()
        response._content = b'{"success": 1}'
        response.status_code = 200

        self.assertFalse(self.retries_handler.is_eligible(response))

    def test_is_eligible_false_due_max_retry_reached(self):
        response = Response()
        response._content = b'{"success": 1}'
        response.status_code = 503
        self.retries_handler.count = 5

        self.assertFalse(self.retries_handler.is_eligible(response))

    def test_is_eligible_true_due_to_error_code(self):
        response = Response()
        response._content = b'{"success": 1}'
        response.status_code = 503

        self.assertTrue(self.retries_handler.is_eligible(response))
