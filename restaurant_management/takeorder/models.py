from django.db import models

class Tables(models.Model):
    number_of_table = models.IntegerField(),
    status_of_table = models.BooleanField(default=True)

class Category(models.Model):
    category_number = models.IntegerField(),
    category_img = models.ImageField(),
    category_name = models.CharField(),

class Menu(models.Model):
    category_number = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(),
    product_price = models.IntegerField(),
    quantity = models.IntegerField(),
    product_img = models.ImageField(),
    
    
class CheckOut(models.Model):
        bill = models.IntegerField(default=0)