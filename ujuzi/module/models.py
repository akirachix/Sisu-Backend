# # from django.db import models
# # from facilitator.models import Facilitator
# # from ujuzi import assessment
# # # from ujuzi import assessment

# # class Module(models.Model):
# #     module_id = models.AutoField(primary_key=True)
# #     facilitator_id = models.ForeignKey(Facilitator, on_delete=models.CASCADE) 
# #     assessment_id = models.ForeignKey(assessment, on_delete=models.CASCADE)   
# #     module_name = models.CharField(max_length=255)
# #     total_marks = models.IntegerField(null=True) 
# #     date_created = models.DateTimeField(auto_now_add=True)
# #     def __str__(self):
# #         return self.module_name


# from django.db import models
# from facilitator.models import Facilitator
# # from ujuzi import module
# # from ujuzi.assessment.models import Assessment

# # Create your models here.
# class Module(models.Model):
#     module_id = models.AutoField(primary_key=True)
#     # module_id = models.ForeignKey(module, on_delete=models.CASCADE)
#     facilitator_id = models.ForeignKey(Facilitator, on_delete=models.CASCADE)
    
#     module_name = models.CharField(max_length=255)
#     total_marks = models.IntegerField(null=True)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def get_assessment(self):
#         from ujuzi.assessment.models import Assessment  # Import inside the function
#         # Logic that uses the `Assessment` model
#         return Assessment.objects.filter(module=self)

#     def __str__(self):
#         return self.module_name

# from facilitator.models import Facilitator

# # Create your models here.
# # class Module(models.Model):
# #     module_id = models.AutoField(primary_key=True)
# #     facilitator_id = models.ForeignKey(Facilitator, on_delete=models.CASCADE)
    
# #     module_name = models.CharField(max_length=255)
# #     total_marks = models.IntegerField(null=True)
# #     date_created = models.DateTimeField(auto_now_add=True)

# #     def get_assessment(self):
# #         from ujuzi.assessment.models import Assessment  # Import inside the function
# #         # Logic that uses the `Assessment` model
# #         return Assessment.objects.filter(module=self)

# #     def __str__(self):
# #         return self.module_name



from django.db import models
from facilitator.models import Facilitator

# Using a string for ForeignKey reference to avoid circular imports.
class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    facilitator = models.ForeignKey(Facilitator, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=255)
    total_marks = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_assessments(self):
        # Import the Assessment model here to avoid circular dependencies
        from ujuzi.assessment.models import Assessment
        return Assessment.objects.filter(module=self)

    def __str__(self):
        return self.module_name
