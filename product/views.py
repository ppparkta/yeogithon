from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import ProductForm
from .models import Product


def product_list(request):
    products = Product.objects.all().order_by('-pk')
    return render(request, 'product/product_list.html', context={'products': products})


# def create_product(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.save()
#             return redirect(reverse('product:product_list'))
#
#     else:
#         form = ProductForm()
#
#     return render(request, 'product/create_product.html', context={'form': form})
#
# # 상품 수정 (권한 필요)
# def edit_product(request, pk):
#     swuni = request.user  # 현재 로그인한 사용자 정보 가져오기
#
#     if not swuni.is_authenticated:  # 권한이 없다면
#         return render(request, 'product/401.html', status=401)  # 401 이동
#
#     product = Product.objects.get(id=pk)
#
#     if request.method == "POST":
#         form = ProductForm(request.POST, instance=product)
#
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.save()
#             return redirect(reverse('product:product_list'))
#
#     else:
#         form = ProductForm()
#
#     return render(request, 'product/create_product.html', context={'form': form})
#
# # 상품 삭제 (권한 필요)
# def delete_product(request, pk):
#     swuni = request.user  # 현재 로그인한 사용자 정보 가져오기
#
#     if not swuni.is_authenticated:  # 권한이 없다면
#         return render(request, 'product/401.html', status=401)  # 401 이동
#
#     if request.method == "POST":
#         product = Product.objects.get(id=pk)
#         product.delete()
#         return redirect(reverse('product:product_list'))
#
#     return render(request, 'product/failDelete.html')

# ---------------- form 미사용 ------------------- #
# 상품 생성 (권한 필요)
def create_product(request):
    swuni = request.user  # 현재 로그인한 사용자 정보 가져오기

    if not swuni.is_authenticated:  # 권한이 없다면
        return render(request, 'product/401.html', status=401)  # 401 이동

    if request.method == "POST":
        productName = request.POST.get('productName')
        productPrice = request.POST.get('productPrice')
        productImage = request.FILES.get('productImage')
        productTemp = request.POST.get('productTemp')

        Product.objects.create(
            productName=productName,
            productPrice=productPrice,
            productImage=productImage,
            productTemp=productTemp
        )
        return redirect(reverse('product:product_list'))

    else:  # GET 요청이면
        return render(request, 'product/create_product.html')


# 상품 수정 (권한 필요)
def edit_product(request, pk):
    swuni = request.user  # 현재 로그인한 사용자 정보 가져오기

    if not swuni.is_authenticated:  # 권한이 없다면
        return render(request, 'product/401.html', status=401)  # 401 이동

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        productName = request.POST.get('productName')
        productPrice = request.POST.get('productPrice')
        productImage = request.FILES.get('productImage')
        productTemp = request.POST.get('productTemp')


        if productImage is None:
            # 새로운 이미지가 제출되지 않은 경우 기존 이미지 유지
            productImage = product.productImage

        # 데이터 변경
        product.productName = productName
        product.productPrice = productPrice
        product.productImage = productImage
        product.productTemp = productTemp

        product.save()

        return redirect(reverse('product:product_list'))

    return render(request, 'product/create_product.html', context={'product': product})


# 상품 삭제 (권한 필요)
def delete_product(request, pk):
    swuni = request.user  # 현재 로그인한 사용자 정보 가져오기

    if not swuni.is_authenticated:  # 권한이 없다면
        return render(request, 'product/401.html', status=401)  # 401 이동

    if request.method == "POST":
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect(reverse('product:product_list'))

    return render(request, 'product/failDelete.html')
