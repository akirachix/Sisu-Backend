from django.db import models

class Kicd(models.Model):
    kicd_id = models.AutoField(primary_key=True)
    teacher_id = models.IntegerField(default=1)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, default =1)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.email}'