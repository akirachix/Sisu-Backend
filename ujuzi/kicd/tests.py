

# Create your tests here.
from django.test import TestCase
from .models import Kicd
from django.core.exceptions import ValidationError

class KicdModelTest(TestCase):
    
    def setUp(self):
        # Set up reusable valid data
        self.valid_teacher_id = 123
        self.valid_first_name = "John"
        self.valid_last_name = "Doe"
        self.valid_email = "john.doe@example.com"
        self.valid_department = "Mathematics"

    # Happy Path: Test successful creation of Kicd model
    def test_kicd_creation(self):
        kicd = Kicd.objects.create(
            teacher_id=self.valid_teacher_id,
            first_name=self.valid_first_name,
            last_name=self.valid_last_name,
            email=self.valid_email,
            department=self.valid_department
        )
        self.assertEqual(kicd.teacher_id, self.valid_teacher_id)
        self.assertEqual(kicd.first_name, self.valid_first_name)
        self.assertEqual(kicd.last_name, self.valid_last_name)
        self.assertEqual(kicd.email, self.valid_email)
        self.assertEqual(kicd.department, self.valid_department)

    # Unhappy Path: Test that an invalid email raises a validation error
    def test_kicd_creation_invalid_email(self):
        invalid_email = "invalid-email"
        with self.assertRaises(ValidationError):
            kicd = Kicd(
                teacher_id=self.valid_teacher_id,
                first_name=self.valid_first_name,
                last_name=self.valid_last_name,
                email=invalid_email,  # Invalid email format
                department=self.valid_department
            )
            kicd.full_clean()  # This triggers validation

    # Unhappy Path: Test missing first_name raises a validation error
    def test_kicd_creation_missing_first_name(self):
        with self.assertRaises(ValidationError):
            kicd = Kicd(
                teacher_id=self.valid_teacher_id,
                last_name=self.valid_last_name,
                email=self.valid_email,
                department=self.valid_department
            )
            kicd.full_clean()  # This triggers validation

    # Unhappy Path: Test that a last_name exceeding max_length raises a validation error
    def test_kicd_creation_last_name_too_long(self):
        long_last_name = "ThisNameIsWayTooLongForTheField"
        with self.assertRaises(ValidationError):
            kicd = Kicd(
                teacher_id=self.valid_teacher_id,
                first_name=self.valid_first_name,
                last_name=long_last_name,  # Exceeds max_length=20
                email=self.valid_email,
                department=self.valid_department
            )
            kicd.full_clean()  # This triggers validation

    # Unhappy Path: Test that missing department raises a validation error
    def test_kicd_creation_missing_department(self):
        with self.assertRaises(ValidationError):
            kicd = Kicd(
                teacher_id=self.valid_teacher_id,
                first_name=self.valid_first_name,
                last_name=self.valid_last_name,
                email=self.valid_email
            )
            kicd.full_clean()  # This triggers validation
