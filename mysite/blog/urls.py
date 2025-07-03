from django.contrib import admin
from django.urls import path
from . import views

# config/urls.py 파일에 모든 요청을 받아서 분배
# config/urls.py 파일에서 guestbook/urls.py를 찾을 수 있게
# config/urls.py    blog/~~~
urlpatterns = [
    path("", views.index),     
    path("list", views.getList), 
]