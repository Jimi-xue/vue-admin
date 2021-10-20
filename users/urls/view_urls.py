from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from users.views import *

urlpatterns = [
    # 认证令牌
    path('token/get', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新令牌
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('userinfo',UserView.as_view(),name='user_info'),
    path('useravatar',UserAvatar.as_view(),name='user_avatar')
]