from django.db import models

# Create your models here.
class MarkingScheme(models.Model):
    markingscheme_id = models.AutoField(primary_key= True)
    module_id = models.IntegerField()
    module_name = models.CharField(max_length=30, default=1)
    date_created = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
     return f'{self.module_name} {self.date_created}'