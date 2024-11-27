from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import MarkingScheme
from django.core.exceptions import ValidationError

class MarkingSchemeModelTest(TestCase):
    
    def setUp(self):
        # Set up any data you want to reuse in tests
        self.valid_module_id = 101
        self.valid_module_name = "Mathematics"
    
    # Happy Path: Test successful creation of MarkingScheme model
    def test_markingscheme_creation(self):
        markingscheme = MarkingScheme.objects.create(
            module_id=self.valid_module_id,
            module_name=self.valid_module_name
        )
        self.assertEqual(markingscheme.module_id, self.valid_module_id)
        self.assertEqual(markingscheme.module_name, self.valid_module_name)
        self.assertIsNotNone(markingscheme.date_created)
    
    # Unhappy Path: Test that an invalid module_name (too long) raises a validation error
    def test_markingscheme_creation_invalid_module_name(self):
        long_module_name = "ThisModuleNameIsWayTooLongAndInvalid"
        with self.assertRaises(ValidationError):
            markingscheme = MarkingScheme(
                module_id=self.valid_module_id,
                module_name=long_module_name
            )
            markingscheme.full_clean()  # This triggers model validation

    # Unhappy Path: Test that missing module_id raises an error
    def test_markingscheme_creation_missing_module_id(self):
        with self.assertRaises(ValidationError):
            markingscheme = MarkingScheme(
                module_name=self.valid_module_name
            )
            markingscheme.full_clean()  # This triggers model validation
