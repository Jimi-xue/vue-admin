from django.urls import path,include
from assets.views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path(r'add_host', HostViewSet.as_view(), ),
    path(r'host/<str:host_name>', HostView.as_view(), ),
    path(r'show_hosts', ShowHostViewSet.as_view(), ),
    # 认证令牌
    path('token/get', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新令牌
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]