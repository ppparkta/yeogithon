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

    if request.method == 'POST':

        swuni = request.user

        if 'product' in request.POST: #cartProduct 보내달라고 fE에게 요청
            # 카트 상품 폼 제출 처리
            cart = Cart.objects.get(swuni=swuni)

            cartProduct_Form = CartProductForm(request.POST)
            if cartProduct_Form.is_valid():

                cartProduct = cartProduct_Form.cleaned_data['cartProductCount', 'cartProduct']
                cartProduct.cart = cart
                # cart.products=cart_product.cartProduct
                # cart_product_list =[]
                # cart_product_list.append(cart.products)
                # cart.products = cart_product_list
                cartProduct.save()
                return render(request, 'product/product_list.html', {'products': products, 'cartProduct': cartProduct})


        elif 'product' in request.POST:

            # 총 가격 계산 요청 처리

            cart = Cart.objects.filter(swuni).first()
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
    return render(request, 'product/product_list.html', {'products': products, 'cartProduct_Form': cartProduct_Form, 'cart_form': cart_form})



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





