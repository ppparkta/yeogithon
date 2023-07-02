from django.urls import path
from user.views import home, oauth_login, Kakao, KakaoCallback, MyPageLikeList, MyPageOrderList

app_name = "user"

urlpatterns = [
    path("", home, name='home'),
    path("login/", oauth_login, name='login'),
    path("oauth/", Kakao.as_view()),
    path("oauth/callback/", KakaoCallback.as_view()),
    path("<int:pk>/likes/", MyPageLikeList, name='like_list'),
    path("<int:pk>/orders/", MyPageOrderList, name='order_list'),
]