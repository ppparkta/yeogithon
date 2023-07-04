from django.urls import path
from cart.views import add_request

app_name = "cart"

urlpatterns = [
    path('', add_request, name='add_request'), #요청작성 뷰 함수
]