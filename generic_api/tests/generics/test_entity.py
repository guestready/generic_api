from django.test import TestCase

from .generic_objects import TestEntity


class GenericEntityTestCase(TestCase):
    def setUp(self):
        self.entity = TestEntity()

    def test_is_valid(self):
        self.assertTrue(self.entity.is_valid())

    def test_data(self):
        self.assertEqual(self.entity.data, {})
