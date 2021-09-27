from django.urls import path,include
from assets.views import *


urlpatterns = [
    path(r'add_host', HostViewSet.as_view(), ),
    path(r'host/<str:host_name>', HostView.as_view(), ),
    path(r'show_hosts', ShowHostViewSet.as_view(), ),
]