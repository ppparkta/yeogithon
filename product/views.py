from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product
from cart.models import Cart
from cart.forms import CartProductForm, CartForm
from cartProduct.models import CartProduct

# 상품 전체 조회 (권한 제한 X)
def product_list(request):
    if not request.user.is_authenticated:
        return redirect('user:login')


    products = Product.objects.all().order_by('-pk')

    if request.method == 'GET':
        return render(request, 'product/product_list.html', context={'products': products})

    # GET 요청 처리 또는 필요한 경우 폼 렌더링
    # cartProduct_Form = CartProductForm()
    return render(request, 'product/product_list.html', {'products': products})

def product_add_cart(request,pk):
    swuni = request.user
    cart, created = Cart.objects.get_or_create(swuni=swuni)
    products = Product.objects.all().order_by('-pk')

    if request.method == 'POST':
        # if 'product' in request.POST:
        product = get_object_or_404(Product, pk=pk)
        count = request.POST.get('count')
        cart_product=CartProduct.objects.create(cart=cart, cartProduct=product, cartProductCount=count)

        # 총 가격 계산
        cart_products = cart.products.all()
        total_price = 0
        for cart_product in cart_products:
            total_price += cart_product.cartProductCount * cart_product.cartProduct.productPrice

        cart.cartTotalPrice = total_price
        cart.save()

        return render(request, 'product/product_list.html', {'products': products, 'cart_product': cart_product, 'cart': cart})
        # return redirect('cart:cart_list', {'cart_product': cartProduct, 'cart': cart})


# 상품 생성 (권한 필요)
def create_product(request):
    swuni = request.user  # 현재 로그인한 사용자 정보 가져오기

    if not swuni.is_authenticated:  # 권한이 없다면
        return redirect('user:login')  # 로그인 페이지 이동

    if request.method == "POST":
        productName = request.POST.get('productName')
        productDetail = request.POST.get('productDetail')
        productPrice = request.POST.get('productPrice')
        productImage = request.FILES.get('productImage')
        productTemp = request.POST.get('productTemp')

        Product.objects.create(
            productName=productName,
            productDetail=productDetail,
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
        return redirect('user:login')  # 로그인 페이지 이동
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        productName = request.POST.get('productName')
        productDetail = request.POST.get('productDetail')
        productPrice = request.POST.get('productPrice')
        productImage = request.FILES.get('productImage')
        productTemp = request.POST.get('productTemp')


        if productImage is None:
            # 새로운 이미지가 제출되지 않은 경우 기존 이미지 유지
            productImage = product.productImage

        # 데이터 변경
        product.productName = productName
        product.productPrice = productPrice
        product.productDetail = productDetail
        product.productImage = productImage
        product.productTemp = productTemp

        product.save()

        return redirect(reverse('product:product_list'))

    return render(request, 'product/create_product.html', context={'product': product})


# 상품 삭제 (권한 필요)
def delete_product(request, pk):
    swuni = request.user  # 현재 로그인한 사용자 정보 가져오기

    if not swuni.is_authenticated:  # 권한이 없다면
        return redirect('user:login')  # 로그인 페이지 이동
    if request.method == "GET":
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect(reverse('product:product_list'))

    return render(request, 'product/failDelete.html')

# 관리자 페이지 이동 버튼
def first_admin(request):
    return render(request, 'product/first_admin.html')





