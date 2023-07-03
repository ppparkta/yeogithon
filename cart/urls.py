from django.urls import path
from cart.views import cart_detail, add_request, get_or_create_cart

app_name = "cart"

urlpatterns = [
    path('', cart_detail, name='cart_list'),
    path('', add_request, name='cart_request'), #요청작성 뷰 함수
    path('', get_or_create_cart, name='get_cart'),
]