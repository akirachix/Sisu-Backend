from django.test import TestCase
from django.db import IntegrityError
from .models import Teacher

class TeacherModelTest(TestCase):

    def setUp(self):
        # This method is called before each test
        self.teacher = Teacher.objects.create(
            tsc_number="123456",
            region="Nairobi",
            school="Nairobi High School",
            teachers_id=1,
            sub_county="Central"
        )

    def test_teacher_creation(self):
        # Test that the teacher was created successfully
        self.assertIsInstance(self.teacher, Teacher)
        self.assertEqual(self.teacher.tsc_number, "123456")
        self.assertEqual(self.teacher.region, "Nairobi")
        self.assertEqual(self.teacher.school, "Nairobi High School")
        self.assertEqual(self.teacher.teachers_id, 1)
        self.assertEqual(self.teacher.sub_county, "Central")

    def test_teacher_string_representation(self):
        # Test the string representation of the teacher
        self.assertEqual(str(self.teacher), "Nairobi Nairobi High School")

    def test_teacher_default_tsc_number(self):
        # Test that the default tsc_number is used if not explicitly provided
        teacher_without_tsc = Teacher.objects.create(
            region="Mombasa",
            school="Mombasa High School",
            teachers_id=2,
            sub_county="Coast"
        )
        self.assertEqual(teacher_without_tsc.tsc_number, "DEFAULT_TSC_NUMBER")

    def test_teacher_required_fields(self):
        # Test that required fields are set properly (i.e., non-null)
        teacher_without_sub_county = Teacher.objects.create(
            tsc_number="789012",
            region="Kisumu",
            school="Kisumu High School",
            teachers_id=3,
            sub_county=""  # Empty sub_county should be allowed (assuming no validation on empty field)
        )
        self.assertEqual(teacher_without_sub_county.sub_county, "")

    # def test_teacher_invalid_creation(self):
    #     # Test that creating a teacher without required fields raises an IntegrityError
    #     with self.assertRaises(IntegrityError):
    #         Teacher.objects.create(
    #             tsc_number="456789",
    #             region="Nakuru",
    #             school="Nakuru High School",
    #             # Missing teachers_id and sub_county, should raise an error
    #         )



# from django.db import IntegrityError
from django.core.exceptions import ValidationError

def test_teacher_invalid_creation(self):
    # Test that creating a teacher without required fields raises a ValidationError
    with self.assertRaises(ValidationError):
        teacher = Teacher(
            tsc_number="456789",
            region="Nakuru",
            school="Nakuru High School",
            # Missing teachers_id and sub_county, should raise an error
        )
        teacher.full_clean()  # This triggers model validation
        teacher.save()  # This will save to the database, which will raise the error
