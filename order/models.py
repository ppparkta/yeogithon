from django.db import models
from cart.models import Cart
from django.utils import timezone
from enum import Enum

class OrderStatus(Enum):
    대기 = '대기'
    취소 = '취소'
    완료 = '완료'

class Order(models.Model):
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE, default=None)
    order_status = models.CharField(max_length=100, choices=[(status.value, status.name) for status in OrderStatus], default=OrderStatus.대기.value)
    order_time = models.DateTimeField(default=timezone.now())