"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

# from pybo import views
# from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pybo/", include('pybo.urls')),
    path("blog/", include("blog.urls")),
    path("guestbook/", include("guestbook.urls")),
    #path("blog/", views.index),     # url이 blog/인 경우 views.py 파일의 index함수 호출
    # path 함수가 url http://127.0.0.1:8000/blog
    # 를 blog/views.py파일의 index 함수를 연동
]
