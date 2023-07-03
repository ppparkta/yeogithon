from django.db import models

# Create your models here.
class Cart(models.Model):
    cartRequest = models.CharField(max_length=100) #장바구니 요청사항
    swuni = models.ForeignKey('user.Swuni', on_delete=models.CASCADE)
    cartTotalPrice = models.IntegerField() #총가격
