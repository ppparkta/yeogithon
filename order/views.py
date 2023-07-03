from django.shortcuts import render, get_object_or_404
from .forms import OrderForm
from .models import Order
from cart.models import Cart
from orderProduct.models import OrderProduct
# Create your views here.


def view_User_Order(request): #사용자 주문 내역 조회
    if request.method == 'GET':
        order = Order.objects.filter(request.user.pk == order.cart.swuni.pk)
        orderProduct.cart_product = cart.products.all()
        order_product_list = orderProduct.cart_product

        return render(request,'order/order_user_list',{'order':order, 'order_product_list': order_product_list})

def view_All_Order(request): #관리자 시점 주문 내역 조회
    if request.method == 'GET':
        order = Order.objects.all()

    # elif request.method == 'POST':
