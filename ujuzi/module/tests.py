from django.test import TestCase
from facilitator.models import Facilitator
from .models import Module

class ModuleModelTest(TestCase):

    def setUp(self):
        # Create a Trainer instance for the foreign key
        self.facilitator = Facilitator.objects.create(
            first_name="Alice",
            last_name="Johnson",
            tsc_number=987654,
            email="alice.johnson@example.com",
            region="Nairobi",
            teachers_id=1
        )

        # Create a Module instance
        self.module = Module.objects.create(
            facilitator_id=self.facilitator,
            module_name="Mathematics",
            total_marks=100
        )

    def test_module_creation(self):
        # Test that the module was created successfully
        self.assertIsInstance(self.module, Module)
        self.assertEqual(self.module.module_name, "Mathematics")
        self.assertEqual(self.module.total_marks, 100)
        self.assertEqual(self.module.facilitator_id, self.facilitator)

    def test_module_string_representation(self):
        # Test the string representation of the module
        self.assertEqual(str(self.module), "Mathematics")

    def test_total_marks_null(self):
        # Test that total_marks can be null
        module_with_null_marks = Module(
            facilitator_id=self.facilitator,
            module_name="Science",
            total_marks=None
        )
        self.assertIsNone(module_with_null_marks.total_marks)
