from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from product import views

app_name = "product"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.create_product, name='create_product'),
]