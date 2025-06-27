from django.contrib import admin
from django.urls import path
from . import views

# config/urls.py 파일에 모든 요청을 받아서 분배
# config/urls.py 파일에서 guestbook/urls.py를 찾을 수 있게
# config/urls.py    guestbook/~~~
urlpatterns = [
    path("", views.index),     
    path("test1", views.test1),
    path("test2/<x>/<y>", views.test2), # def test2(request, x, y)  변수명이 같아야 함.
    path("test3", views.test3),
    path("sigma/<num>", views.sigma),
    path("isLeap", views.isLeap),
    path("calc/<s>/<x>/<y>", views.calc),
    path("list", views.list),
    path("write", views.write),
    path("save", views.save),
    
    path("add_write", views.add_write),
    path("add_save", views.add_save),

    # json형식으로 응답
    path("getData", views.getData),
    path("userInfo", views.userInfo),
]






