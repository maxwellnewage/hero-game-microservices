from uuid import UUID

from django.test import TestCase
from .models import User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.maxwell = User.objects.create_user(
            "maxwell",
            "max@mail.com",
            "123"
        )

    def test_user_exists(self):
        self.assertIsNotNone(self.maxwell)

    def test_user_id_correct(self):
        self.assertIsNotNone(self.maxwell.id)
        self.assertIsInstance(self.maxwell.id, UUID)
