from django.db import models

class Tables(models.Model):
    number_of_table = models.IntegerField(),
    status_of_table = models.BooleanField(default=True)