from datetime import datetime
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200,unique=True)
    price = models.DecimalField(max_digits=12,decimal_places=2)
    quantity_in_stock = models.IntegerField()

# class addproduct(models.Model):
#     sku = models.CharField(max_length=200,unique=True)

class coupon(models.Model):
    code = models.CharField(max_length=200)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField()
    sku = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity_in_stock = models.IntegerField()