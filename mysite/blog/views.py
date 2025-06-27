from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

# 웹에서 정보를 요청하면 이 페이지가 호출된다.
def index(request):
    return HttpResponse("Hello Django");

# 이 함수와 url을 연결하는 작업이 필요하다.
# http://127.0.0.1/blog ==> blog/views.py파일의 index가 호출되게 한다.


