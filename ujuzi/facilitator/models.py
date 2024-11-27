from django.db import models

# Create your models here.

class Facilitator(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tsc_number = models.IntegerField()
    email = models.EmailField()
    region = models.CharField(max_length=100)
    teachers_id = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"