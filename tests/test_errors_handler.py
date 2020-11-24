from django.test import TestCase
from requests.exceptions import HTTPError
from requests.models import Response

from generic_api.errors_handler import HttpErrorsHandler


class GenericErrorsHandlerTestCase(TestCase):
    def setUp(self):
        self.errors_handler = HttpErrorsHandler()

    def test_response_valid(self):
        response = Response()
        response._content = b'{"success": 1}'
        response.status_code = 200

        self.assertEqual(self.errors_handler.validate(response), {'success': True})

    def test_response_invalid(self):
        response = Response()
        response._content = b'{"success": 0}'
        response.status_code = 400

        with self.assertRaises(HTTPError):
            self.errors_handler.validate(response)
