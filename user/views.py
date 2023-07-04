from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import View, CreateView, UpdateView, DeleteView

import order.models
import post.models
from cart.models import Cart
from order.models import Order
from orderProduct.models import OrderProduct
from .models import Swuni
import requests

# Create your views here.

# 로그인 템플릿
def oauth_login(request):
    return render(request, './user/login.html', {})

# def home(request):
#     return render(request, './user/home.html', {})

# 인가 코드 요청
class Kakao(View):
    def get(self, request):
        kakao_api="https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri="http://127.0.0.1:8000/users/oauth/callback"
        client_id="d487e9f9d02f41bcef124574ed5ffe64"
        return redirect(f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}")

# 토큰 발급 및 회원가입
class KakaoCallback(View):
    def get(self, request):
        data = {
            "grant_type":"authorization_code",
            "client_id":"d487e9f9d02f41bcef124574ed5ffe64",
            "redirection_uri":"http://127.0.0.1:8000/users/oauth",
            "code":request.GET["code"]
        }
        kakao_token_api="https://kauth.kakao.com/oauth/token"
        access_token = requests.post(kakao_token_api, data=data).json().get("access_token")
        if access_token==None:
            return JsonResponse({'message': 'INVALID_TOKEN'}, status=401)
        #카카오 사용자 정보 요청
        kakao_user_api="https://kapi.kakao.com/v2/user/me"
        user_info=requests.get(kakao_user_api, headers={"Authorization":f"Bearer ${access_token}"}).json()
        # print(user_info)
        if not Swuni.objects.filter(kakaoId=user_info['id']).exists():
            swuni=Swuni.objects.create(
                kakaoId=user_info['id'],
                userName=user_info['properties']['nickname'],
                userImage=user_info['properties']['thumbnail_image'],
                last_login=timezone.now(),
                password="1234",
            )
            cart=Cart.objects.create(
                cartTotalPrice=0,
                swuni=swuni,
            )
        # 로그인
        swuni = Swuni.objects.get(kakaoId=user_info['id'])
        login(request, swuni, 'user.auth.MyBackend')
        return redirect('http://127.0.0.1:8000/users/')

# 마이페이지-찜 게시글 목록
def MyPageLikeList(request, pk):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'user/login.html', status=401)
        if not request.user.pk == pk:
            return render(request, 'user/403.html', status=403)
        list = post.models.Post.objects.filter(like=pk)
        return render(request, 'user/mypageLikes.html', { "likes": list })

# 마이페이지-주문 목록
def MyPageOrderList(request, pk):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'user/login.html', status=401)
        if not request.user.pk == pk:
            return render(request, 'user/403.html', status=403)
        cart = Cart.objects.get(swuni=request.user)
        list = Order.objects.filter(cart=cart)
        return render(request, 'user/mypageOrders.html', { "orders": list })
