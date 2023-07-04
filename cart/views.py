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

            order = Order.objects.create(cart=cart)
            for cart_product in cart.products.all():
                order_product = OrderProduct.objects.create(order=order, cart_product=cart_product)
            order.save()

            cart.cartRequest = ''
            cart.cartTotalPrice = 0
            # return order, order_product
        return redirect('product:product_list')  # 상품 목록페이지

    elif request.method == 'GET':
        cart = Cart.objects.filter(swuni=swuni).first()
        cart_product_list = cart.products.all()

        return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_product_list': cart_product_list})
