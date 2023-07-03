from django.db import models
from cart.models import Cart

class Order(models.Model):
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE)  # 카트와의 외래키 연결
    order_status = models.CharField(max_length=100, null=True, blank=True)  # 주문 상태 필드 (예: 처리 중, 완료 등)
    order_time = models.DateTimeField(auto_now_add=True)  # 주문 시간 필드
    # OrderProduct = models.ForeignKey('orderProduct.OrderProduct', on_delete=models.CASCADE) #주문 상품과 연결

