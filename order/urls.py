from django.urls import path
from order.views import view_all_order

app_name = "order"

urlpatterns = [
    path('admin/', view_all_order, name='view_all_order'),
]
