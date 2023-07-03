from django.shortcuts import render
from .forms import OrderForm
from .models import Order
from cart.models import Cart
# Create your views here.

def create_Order(request):
    if request.method == 'POST':
        # 카트 정보 가져오기
        cart = get_object_or_404(Cart, pk=cart_id)

        # 주문 객체 생성
        order = Order.objects.create(cart=cart, order_status='주문 처리 중', OrderProduct=cart.cart_product_list)

        return render(request, 'product/product_list.html', {'message': '주문이 성공적으로 생성되었습니다.'})
    else:
        # GET 요청 처리 로직 작성
        return render(request, 'cart/cart_list.html')

