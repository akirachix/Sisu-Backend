from django.db import models

class Teacher(models.Model):
    tsc_number = models.CharField(max_length=100, default="DEFAULT_TSC_NUMBER")
    region = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    teachers_id = models.IntegerField(null=True)
    sub_county = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.region} {self.school}"
