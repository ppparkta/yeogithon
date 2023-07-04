from django.db import models
from order.models import Order
from cartProduct.models import CartProduct
# Create your models here.
class OrderProduct(models.Model):
    order = models.ForeignKey('order.Order', related_name='products', on_delete=models.CASCADE)
    cart_product = models.ForeignKey(CartProduct, on_delete=models.CASCADE, default=None)
