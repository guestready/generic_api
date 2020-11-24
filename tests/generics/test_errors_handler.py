from django.test import TestCase

from .generic_objects import TestErrorsHandler


class GenericErrorsHandlerTestCase(TestCase):
    def setUp(self):
        self.errors_handler = TestErrorsHandler()

    def test_validate(self):
        class TestResponse:
            @property
            def data(self):
                return {}

        self.assertEqual(self.errors_handler.validate(TestResponse()), {})
