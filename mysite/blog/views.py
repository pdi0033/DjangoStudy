from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse

# Create your views here.

# 웹에서 정보를 요청하면 이 페이지가 호출된다.
def index(request):
    return HttpResponse("Hello Django");

# 이 함수와 url을 연결하는 작업이 필요하다.
# http://127.0.0.1/blog ==> blog/views.py파일의 index가 호출되게 한다.

from blog.models import BlogModel
from django.core import serializers

# http://127.0.0.1:8000/blog/list
def getList(request):
    dataSet = list(BlogModel.objects.values())
    # 직렬화 - 객체를 파일이나 네트워크로 출력하고자 하는 걸 직렬화
    #data = serializers.serialize("json", dataSet)
    # json_dumps_params={'ensure_ascii':False} 한글 깨짐 방지
    return JsonResponse(dataSet, safe=False, json_dumps_params={'ensure_ascii':False})

