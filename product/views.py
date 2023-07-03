from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product
from cart.models import Cart
from cart.forms import CartProductForm, CartForm
from cartProduct.models import CartProduct

# 상품 전체 조회 (권한 제한 X)
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all().order_by('-pk')
        return render(request, 'product/product_list.html', context={'products': products})

    if request.method == 'POST':
        if 'cartProduct' in request.POST:
            # 카트 상품 폼 제출 처리
            cart = Cart.objecst.filter(request.user.pk == swuni.pk)
            cartProduct_Form = CartProductForm(request.POST)
            if cartProduct_Form.is_valid():
                cart_product = cartProduct_Form.save(commit=False)
                cart_product.cart = cart
                cart_product.save()
                return render(request, 'product/product_list.html', {'product': product, 'cart_product': cart.products.all()})


        elif 'calculateTotalPrice' in request.POST:

            # 총 가격 계산 요청 처리

            cart = Cart.objecst.filter(request.user.pk == swuni.pk)

            cart_product_list = cart.products.all()

            total_price = 0

            for cart_product in cart_product_list:
                total_price += cart_product.cartProductCount * cart_product.cartProduct.price

            cart.cartTotalPrice = total_price

            cart.save()

            return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_product_list': cart_product_list})

    # 다른 경우 처리 또는 필요한 경우 폼을 다시 렌더링
    cartProduct_Form = CartProductForm()
    cart_form = CartForm()
    return render(request, 'product/product_list.html', {'cartProduct_Form': cartProduct_Form, 'cart_form': cart_form})



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

    if request.method == "GET":
        product = Product.objects.get(id=pk)
        product.delete()
        return redirect(reverse('product:product_list'))

    return render(request, 'product/failDelete.html')
