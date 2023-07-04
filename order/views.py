from django.shortcuts import render
import cart.views
from .forms import OrderForm
from .models import Order
from orderProduct.models import OrderProduct
# Create your views here.


# 전체 주문 조회 (GET), 주문 상태 변경 (POST)
def view_all_order(request, pk):
    if request.method == 'GET':
        order = Order.objects.all()

        return render(request, 'order/admin_order_list', {'order': order})

    if request.method == 'POST':
        if 'order_status_cancel' in request.POST:
            order = Order.objects.get(pk=pk)
            order.order_status = '취소'
            order.save()

        elif 'order_status_success' in request.POST:
            order = Order.objects.get(pk=pk)
            order.order_status = '완료'
            order.save()
