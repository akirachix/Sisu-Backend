from django.test import TestCase
from teacher.models import Teacher
from module.models import Module
from kicd.models import Kicd
from .models import Assessment
from facilitator.models import Facilitator

class AssessmentModelTest(TestCase):

    def setUp(self):
        # Create instances of related models for foreign keys
        self.facilitator = Facilitator.objects.create(
            tsc_number=987654,
            region="Nairobi",
            teachers_id=1
        )

        self.teacher = Teacher.objects.create(
            tsc_number=123456,
            region="Nairobi",
            teachers_id=2
        )

        self.module = Module.objects.create(
            facilitator_id=self.facilitator,
            module_name="Mathematics",
            total_marks=100
        )

        # Create an instance of Kicd using actual fields
        self.kicd = Kicd.objects.create(
            teacher_id=1,  # Default or appropriate ID
            department="Mathematics"
        )

        # Create an Assessment instance
        self.assessment = Assessment.objects.create(
            module_id=self.module,
            teacher_id=self.teacher,
            kicd_id=self.kicd,
            date_created="2023-10-01",
            total_marks=100,
            assessment_duration=60
        )

    def test_assessment_creation(self):
        # Test that the assessment was created successfully
        self.assertIsInstance(self.assessment, Assessment)
        self.assertEqual(self.assessment.total_marks, 100)
        self.assertEqual(self.assessment.assessment_duration, 60)
        self.assertEqual(self.assessment.module_id, self.module)
        self.assertEqual(self.assessment.teacher_id, self.teacher)
        self.assertEqual(self.assessment.kicd_id, self.kicd)

    def test_assessment_string_representation(self):
        # Test the string representation of the assessment
        self.assertEqual(str(self.assessment), f"Assessment {self.assessment.assessment_id} - Module {self.module.module_name}")

    def test_kicd_id_can_be_null(self):
        # Test that kicd_id can be null
        assessment_without_kicd = Assessment(
            module_id=self.module,
            teacher_id=self.teacher,
            date_created="2023-10-01",
            total_marks=80,
            assessment_duration=45,
            kicd_id=None  # kicd_id is allowed to be null
        )
        self.assertIsNone(assessment_without_kicd.kicd_id)
