from django.db import models

# Create your models here.
class OrderProduct(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE) #상품
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE) # 주문
    count = models.IntegerField() # 수량
