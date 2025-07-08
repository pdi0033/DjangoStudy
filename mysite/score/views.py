from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpRequest, HttpResponse, JsonResponse
# Create your views here.

from .models import Score

def index(request):
    return redirect("score:score_list")

def list(request):      # 데이터 여러 개 가져오기
    scoreList = Score.objects.all()
    return render(request, "score/score_list.html", 
                  {"scoreList":scoreList, "title":"성적처리"})

def view(request, id):  # 데이터 한 개 가져오기
    return render(request, "score/score_view.html")

def write(request):
    return render(request, "score/score_write.html")

def save(request):      # 데이터 저장
    return redirect("score:score_list")

