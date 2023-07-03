from django.shortcuts import render, redirect
from .forms import CartProductForm, CartForm
from cartProduct.models import CartProduct
from .models import Cart
from order.models import Order
#
#폼으로 입력 받아서 장바구니 요청사항 생성후 카트 저장
def add_request(request, cart_id):

    if request.method == 'POST':
        cart = Cart.objecst.filter(request.user.pk == swuni.pk)
        cart_form = CartForm(request.POST)

        if cart_form.is_valid():
            cart_request = cart_form.cleaned_data['cartRequest']
            cart.cartRequest = cart_request
            cart.save()

            order = Order.objects.create(cart=cart, order_status='주문 처리 중', OrderProduct=cart.cart_product_list)
            order.save()

            return redirect('http://127.0.0.1:8000/products')  # 장바구니 상세 페이지로 리디렉션

    elif request.method == 'GET':
        cart = Cart.objecst.filter(request.user.pk == swuni.pk)

        cart_product_list = cart.products.all()

        return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_product_list': cart_product_list})

# def create_Order(request): #장바구니 화면에서 주문하기 누르면 만들어짐
#     if request.method == 'POST':
#         # 카트 정보 가져오기
#         cart = Cart.objecst.filter(request.user.pk == swuni.pk)
#
#         # 주문 객체 생성
#         order = Order.objects.create(cart=cart, order_status='주문 처리 중', OrderProduct=cart.cart_product_list)
#
#         return render(request, 'product/product_list.html', {'message': '주문이 성공적으로 생성되었습니다.'})
#     else:
#         # GET 요청 처리 로직 작성
#         return render(request, 'cart/cart_list.html')