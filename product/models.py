from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=20) # 상품명
    productPrice = models.IntegerField() # 가격
    productImage = models.ImageField(upload_to='', blank=False) # 상품 사진
    productTemp = models.BooleanField(default=True) # True -> ice, False -> hot, default 값은 ice로

    def __str__(self):
        return f'{self.productName}'
