"""vueproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView
from .view import SwaggerSchemaView

api_urlpatterns = [
    path(r'api/assets/', include('assets.urls.view_urls')),
    path(r'api/users/', include('users.urls.view_urls')),
    re_path(r'^api/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', TemplateView.as_view(template_name="index.html")),
    path(r'docs/',  SwaggerSchemaView.as_view(), name='apiDocs'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += api_urlpatterns