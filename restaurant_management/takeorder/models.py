from django.db import models

class Tables(models.Model):
    table_number = models.IntegerField()
    status_of_table = models.BooleanField(default=False)
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()    
    
    def __str__(self):
        return self.name
