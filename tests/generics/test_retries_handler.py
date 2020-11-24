from django.test import TestCase

from .generic_objects import TestRetriesHandler


class GenericRetriesHandlerTestCase(TestCase):
    def setUp(self):
        self.retries_handler = TestRetriesHandler()

    def test_is_eligible(self):
        self.assertFalse(self.retries_handler.is_eligible({}))
