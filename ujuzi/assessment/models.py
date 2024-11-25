from django.db import models

# Create your models here.
from django.db import models
from teacher.models import Teacher
from module.models import Module
from kicd.models import Kicd

class Assessment(models.Model):
    assessment_id = models.AutoField(primary_key=True)
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    kicd_id = models.ForeignKey(Kicd, on_delete=models.CASCADE, null=True, blank=True)  
    question = models.TextField()
    date_created = models.DateField()
    total_marks = models.IntegerField()
    assessment_duration = models.IntegerField()  
    def __str__(self):
        return f"Assessment {self.assessment_id} - Module {self.module_id.module_name}"
    
   