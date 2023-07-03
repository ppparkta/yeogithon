from django.shortcuts import render, redirect
from .forms import CartProductForm, CartForm
from cartProduct.models import CartProduct
from .models import Cart

# def create_cartProduct(request):
#     if request.method == 'POST':
#         cartProduct_Form = CartProductForm(request.POST)
#         if cartProduct_Form.is_valid():
#             cartProduct = cartProduct_Form.save(commit=False)
#             cartProduct.save()  # 카트 상품 저장
#
#             # 카트 상품을 카트의 리스트에 추가
#             cart = cartProduct.cart
#             cart.cartproduct_set.add(cartProduct)
#
#             # return redirect('cart:cart_detail')  # 메뉴판 유지 해야함 수정 필요
#             return render(request, 'product/product_list.html',
#                           {'cartProduct_Form': cartProduct_Form, 'cartProduct_list': cartProduct_list})
#     else:
#         cartProduct_Form = CartProductForm()
#
#     # cartProduct_list = CartProduct.objects.all()  # 카트 상품 리스트 조회 -> 없어도 됨
#
#     return render(request, 'product/product_list.html',
#                   {'cartProduct_Form': cartProduct_Form, 'cartProduct_list': cartProduct_list})
#
# def create_cart(request):
#     if request.method == 'POST':
#         cart_form = CartForm(request.POST)
#         if cart_form.is_valid():
#             cart = cart_form.save()  # 카트 폼 데이터 저장 및 Cart 객체 반환
#             return render(request, 'product/product_list.html')  # 메뉴판 페이지를 다시 렌더링
#     else:
#         cart_form = CartForm()  # 빈 카트 폼 인스턴스 생성
#
#     return render(request, 'cart/create_cart.html', {'cart_form': cart_form})
#
#
# def create_cartProduct(request, cart_product_list=None):
#     if request.method == 'POST':
#         cartProduct_Form = CartProductForm(request.POST)
#         cart_Form = CartForm(request.POST)
#         if cartProduct_Form.is_valid() and cart_Form.is_valid():
#             cart = cart_Form.save()  # 카트 폼 데이터 저장 및 Cart 객체 반환
#             cart_Product = cartProduct_Form.save(commit=False)
#             cart_Product.cart = cart
#             cart_Product.save()
#
#             if cart_product_list is not None:
#                 for cart_product_data in cart_product_list:
#                     cart_product = CartProduct.objects.create(
#                         cart=cart,
#                         cartProductCount=cart_product_data['cartProductCount'],
#                         cartProduct=cart_product_data['cartProduct']
#                     )
#
#             return redirect('cart:cart_detail')  # 카트 상세 페이지로 리디렉션
#     else:
#         cartProduct_Form = CartProductForm()  # 빈 카트 상품 폼 인스턴스 생성
#         cart_Form = CartForm()  # 빈 카트 폼 인스턴스 생성
#
#     return render(request, 'cart/create_cartProduct.html',
#                   {'cartProduct_Form': cartProduct_Form, 'cart_Form': cart_Form})
#
#
# def create_cart(request):
#     if request.method == 'POST':
#         cart_product_list = request.POST.getlist('cart_product')
#         cart_form = CartForm(request.POST)
#         if cart_form.is_valid():
#             cart = cart_form.save()  # 카트 폼 데이터 저장 및 Cart 객체 반환
#
#             if cart_product_list:
#                 for cart_product_data in cart_product_list:
#                     cart_product_count = cart_product_data.get('cartProductCount')
#                     cart_product_id = cart_product_data.get('cartProduct')
#
#                     CartProduct.objects.create(
#                         cart=cart,
#                         cartProductCount=cart_product_count,
#                         cartProduct_id=cart_product_id
#                     )
#
#             return render(request, 'product/product_list.html')  # 메뉴판 페이지를 다시 렌더링
#     else:
#         cart_form = CartForm()  # 빈 카트 폼 인스턴스 생성
#
#     return render(request, 'cart/create_cart.html', {'cart_form': cart_form})
# 카트 상품 리스트

# def create_cartProduct(request):
#     if request.method == 'POST':
#         cartProduct_Form = CartProductForm(request.POST)
#         cart_Form = CartForm(request.POST)
#         if cartProduct_Form.is_valid() and cart_Form.is_valid():
#             cart_Product = cartProduct_Form.save(commit=False)
#
#             # 카트 상품 리스트에 추가
#             cart_product_list.append(cart_Product)
#
#             return render(request, 'product/product_list.html')  # 메뉴판 페이지를 다시 렌더링
#     else:
#         cartProduct_Form = CartProductForm()  # 빈 카트 상품 폼 인스턴스 생성
#         cart_Form = CartForm()  # 빈 카트 폼 인스턴스 생성
#
#     return render(request, 'product/product_list.html',
#                   {'cartProduct_Form': cartProduct_Form, 'cart_Form': cart_Form})
#
#
# def addProduct_cart(request): #카트에 카트 상품 넣기
#     if request.method == 'POST':
#         cart = Cart.objects.create()  # 카트 객체 생성
#
#         for cart_product in cart_product_list:
#             cart_product.cart = cart
#             cart_product.save()
#
#         total_price = 0
#         for cart_product in cart_product_list:
#             total_price += cart_product.cartProductCount * cart_product.cartProduct.price
#
#         cart.cartTotalPrice = total_price
#         cart.save()
#
#         return render(request, 'cart/cart_list.html')  # 장바구니 화면
#     else:
#         return render(request, 'cart/cart_list.html') #장바구니 화면으로 이동
#
#
# def add_request(request, cart_id): #장바구니 요청 사항 넣기
#     cart = get_object_or_404(Cart, pk=cart_id)
#     if request.method == 'POST':
#         cart_form = CartForm(request.POST)
#         if cart_form.is_valid():
#             cart_request = cart_form.cleaned_data['cartRequest']
#             cart.cartRequest = cart_request
#             cart.save()
#             return render(request, 'cart/cart_list.html')  # 장바구니 상세 페이지로 리디렉션
#     else:
#         cart_form = CartForm()
#
#     return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_form': cart_form})
#
#
# def cart_detail(request):
#     # 장바구니 조회
#     cart = get_object_or_404(Cart, pk=cart_id)
#
#     # 장바구니 상품 리스트 조회
#     cart_product_list = cart.products.all()
#
#     return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_product_list': cart_product_list})
#     #총 가격과 요청사항은 템플릿에 cart.cartRequest, cart.cartTotalPrice
#

#메뉴판에서 상품을 선택했을 때 그 상품이 카트 상품으로 인식
def create_cartProduct(request):
    if request.method == 'POST':
        cartProduct_Form = CartProductForm(request.POST)
        if cartProduct_Form.is_valid():
                cart_Product = cartProduct_Form.save(commit=False)

                # 카트 상품 리스트에 추가
                cart_product_list.append(cart_Product)

                return render(request, 'product/product_list.html')   # 상품 리스트 페이지로 리디렉션
    else:
        cartProduct_Form = CartProductForm()  # 빈 카트 상품 폼 인스턴스 생성

    return render(request, 'product/product_list.html',
                  {'cartProduct_Form': cartProduct_Form, 'cart_Form': cart_Form})


#카트 생성 + 위에서 만든 카트 상품 리스트를 카트에 넣음
#카트 상품 리스트에 담긴 상품들의 총가격 계산한 후 카트 저장
def addProduct_cart(request):
    if request.method == 'POST':
        # 현재 사용자의 카트 가져오기 또는 생성하기
        cart = get_or_create_cart(request)

        for cart_product in cart_product_list:
            cart_product.cart = cart
            cart_product.save()

        # cart.products = cart_product_list
        #요청사항 작성

        total_price = 0
        for cart_product in cart_product_list:
            total_price += cart_product.cartProductCount * cart_product.cartProduct.price

        cart.cartTotalPrice = total_price
        cart.save()

        return render(request, 'cart/cart_list.html')  # 장바구니 화면
    else:
        return render(request, 'cart/cart_list.html')  # 장바구니 화면으로 이동


#폼으로 입력 받아서 장바구니 요청사항 생성후 카트 저장
def add_request(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    if request.method == 'POST':
        cart_form = CartForm(request.POST)
        if cart_form.is_valid():
            cart_request = cart_form.cleaned_data['cartRequest']
            cart.cartRequest = cart_request
            cart.save()
            return render(request, 'cart/cart_list.html')  # 장바구니 상세 페이지로 리디렉션
    else:
        cart_form = CartForm()

    return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_form': cart_form})


#장바구니 조회
def cart_detail(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)

    cart_product_list = cart.products.all()

    return render(request, 'cart/cart_list.html', {'cart': cart, 'cart_product_list': cart_product_list})


def get_or_create_cart(request):
    # 세션에서 카트 아이디 가져오기
    cart_id = request.session.get('cart_id')

    if cart_id:
        # 기존 카트가 있는 경우 해당 카트 반환
        cart = get_object_or_404(Cart, pk=cart_id)
    else:
        # 기존 카트가 없는 경우 새로운 카트 생성
        cart = Cart.objects.create()
        # 세션에 카트 아이디 저장
        request.session['cart_id'] = cart.id

    return cart
