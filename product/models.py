from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(max_length=20)
    productPrice = models.IntegerField()
    productImage = models.ImageField()
    productTemp = models.BooleanField(default=True) #True -> ice, False -> hot, default 값은 ice로
    productCategory = models.CharField(max_length=10)