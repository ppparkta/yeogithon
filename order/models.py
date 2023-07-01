from django.db import models

# Create your models here.

class Order(models.Model):
    swuni = models.ForeignKey('user.Swuni', on_delete=models.CASCADE) # 사용자
    orderRequest = models.CharField(max_length=100) # 요청 사항
    orderState = models.CharField(max_length=20) # 주문 상태

