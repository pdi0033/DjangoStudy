from django.contrib import admin
from django.urls import path
from . import views

# config/urls.py 파일에 모든 요청을 받아서 분배
# config/urls.py 파일에서 guestbook/urls.py를 찾을 수 있게
# config/urls.py    score/~~~
app_name = "score"       # 반드시 필요함.
urlpatterns = [
    path("", views.index),     
    path("list", views.list, name="score_list"),          # html
    path("view/<id>", views.view, name="score_view"),        # html에서 url 'score:score_view'
    path("write", views.write, name="score_write"),        # html페이지로 이동
    path("save", views.save, name="score_save"),          # 데이터를 받아서 디비에 저장
]