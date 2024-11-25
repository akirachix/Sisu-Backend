from django.test import TestCase
from .models import Facilitator
from django.core.exceptions import ValidationError

class FacilitatorModelTest(TestCase):

    def setUp(self):
        # This method is called before each test
        self.facilitator = Facilitator.objects.create(
            first_name="Alice",
            last_name="Johnson",
            tsc_number=987654,
            email="alice.johnson@example.com",
            region="Nairobi",
            teachers_id=1
        )

    def test_facilitator_creation(self):
        # Test that the facilitator was created successfully
        self.assertIsInstance(self.facilitator, Facilitator)
        self.assertEqual(self.facilitator.first_name, "Alice")
        self.assertEqual(self.facilitator.last_name, "Johnson")
        self.assertEqual(self.facilitator.tsc_number, 987654)
        self.assertEqual(self.facilitator.email, "alice.johnson@example.com")
        self.assertEqual(self.facilitator.region, "Nairobi")
        self.assertEqual(self.facilitator.teachers_id, 1)

    def test_facilitator_string_representation(self):
        # Test the string representation of the facilitator
        self.assertEqual(str(self.facilitator), "Alice Johnson")

    def test_email_validation(self):
        # Test that an invalid email raises a ValidationError
        facilitator_with_invalid_email = Facilitator(
            first_name="Bob",
            last_name="Smith",
            tsc_number=123456,
            email="invalid-email",  # Invalid email format
            region="Mombasa",
            teachers_id=2
        )
        
        with self.assertRaises(ValidationError):
            facilitator_with_invalid_email.full_clean()  # This will validate the instance
