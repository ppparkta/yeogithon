from django.db import models
from cart.models import Cart

# Create your models here.
class CartProduct(models.Model):
    cartProductCount = models.IntegerField() #수량
    cartProduct = models.ForeignKey('product.Product', on_delete=models.CASCADE) #상품이랑 외래키
    cart = models.ForeignKey('cart.Cart', related_name='products', on_delete=models.CASCADE)
    cartProductTemp = models.BooleanField(default=True)