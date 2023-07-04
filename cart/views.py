from django.shortcuts import render, redirect
from .forms import CartProductForm, CartForm
from cartProduct.models import CartProduct
from .models import Cart
from order.models import Order
from orderProduct.models import OrderProduct
from user.models import Swuni
#폼으로 입력 받아서 장바구니 요청사항 생성후 카트 저장
def add_request(request):
    swuni = request.user
    if request.method == 'POST':
        cart = Cart.objects.filter(swuni=swuni).first()


        cart_form = CartForm(request.POST)

        if cart_form.is_valid():
            cart_request = cart_form.cleaned_data['cartRequest']
            cart.cartRequest = cart_request
            cart.save()

            order = Order.objects.create(cart=cart, order_status='주문 처리 중', OrderProduct=cart.cart_product_list)
            order_product = OrderProduct(order=order, cartProduct=cart.products.all())
            order_product.save()
            order.save()

            cart.cartRequest.clear()
            cart.cartTotalPrice.clear()
            return order, order_product

        return redirect('http://127.0.0.1:8000/products')  # 장바구니 상세 페이지로 리디렉션

    elif request.method == 'GET':
        cart = Cart.objects.filter(swuni=swuni).first()


        cart_product_list = cart.products.all()

        return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_product_list': cart_product_list})


