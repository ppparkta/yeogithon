from django.shortcuts import render, redirect
import cart.views
from .forms import OrderForm
from .models import Order, OrderStatus
from orderProduct.models import OrderProduct
# Create your views here.


def view_all_order(request):
    if request.method == 'POST':
        if 'order_status_cancel' in request.POST:
            selected_orders = request.POST.getlist('menu')
            for order_id in selected_orders:
                order = Order.objects.get(pk=order_id)
                order.order_status = '취소'
                order.save()

        elif 'order_status_success' in request.POST:
            selected_orders = request.POST.getlist('menu')
            for order_id in selected_orders:
                order = Order.objects.get(pk=order_id)
                order.order_status = '완료'
                order.save()

    orders = Order.objects.all()
    return render(request, 'order/admin_order_list.html', {'order': orders})