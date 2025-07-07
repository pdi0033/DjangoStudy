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

def write(request):     # blog_write.html 페이지로 이동
    return render(request, "blog/blog_write.html", {})

# .은 나랑 같은 디렉토리
# forms forms.py 파일명
# BlogForms 클래스 가져오기
from .forms import BlogForms
from django.utils import timezone
from django.shortcuts import redirect
def save(request):
    form = BlogForms(request.POST)      # form.fieldList에 있는 title에
                                        # form 태그의 title값이 들어온다.
    blogModel = form.save(commit=False)     # 디비 저장이 끝남. 완료아님
    # 리턴이 모델을 반환함.
    blogModel.wdate = timezone.now()
    blogModel.hit = 0
    blogModel.save()        # 확정하기

    # 저장을 하고 나면 글목록으로 이동
    # 직접 blog_list 메서드 호출하면 안 된다. 
    # 글 등록 후 request 객체에 있는 내용을 비우고 정리 작업을 해야 한다.
    # 클라이언트로부터 다시 list 요청이 온 것처럼 해야 한다.
    return redirect("blog:blog_list")
# app_name 등록 blog
# name="blog_list"


