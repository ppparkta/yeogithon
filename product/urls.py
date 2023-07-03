from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from product import views
from cart.views import create_cartProduct, addProduct_cart

app_name = "product"

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.create_product, name='create_product'),
    path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/delete/', views.delete_product, name='delete_product')
    path('create_cartProduct', create_cartProduct, name='create_cartProduct'),
    path('add-product/', addProduct_cart, name='addProduct_cart'),

]