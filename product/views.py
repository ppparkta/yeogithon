from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ProductForm
from .models import Product
def product_list(request):
    products = Product.objects.all().order_by('pk')
    return render(request, 'product/product_list.html', {'products': products})

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect(reverse('product:product_list'))

    else:
        form = ProductForm()

    return render(request, 'product/create_product.html', context={'form': form})
