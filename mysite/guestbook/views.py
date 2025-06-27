from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
# JsonResponse - dict => json으로 바꿔서 응답하는 클래스
# Create your views here.

def index(request):
    return HttpResponse("guestbook");

# GET 방식이 파라미터 전달방식1
# x=1&y=1  << 파라미터라고 부른다.
# http://127.0.0.1:8000/guestbook/test1?x=5&y=7
def test1(request):
    x = request.GET.get("x")
    y = request.GET.get("y")
    return HttpResponse(int(x) + int(y))

# GET 방식이 파라미터 전달방식2
# 최신식. 권장 코드
# http://127.0.0.1:8000/guestbook/test2/5/7
def test2(request, x, y):
    return HttpResponse(int(x)+int(y))

# POST 방식
def test3(request):
    if request.method == "POST":
        x = request.POST.get("x")
        y = request.POST.get("y")
        return HttpResponse(int(x) + int(y))
    else:
        return HttpResponse("Error")

# 1. http://127.0.0.1:8000/guestbook/sigma/10       1~10까지의 합계 반환하기
def sigma(request, num):
    sum = 0
    for i in range(1, int(num)+1):
        sum += i
    return HttpResponse(sum)

# 2. http://127.0.0.1:8000/guestbook/isLeap?year=2025   윤년이면 윤년 아니면 윤년이 아니다.
def isLeap(request):
    year = int(request.GET.get("year"))
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return HttpResponse("윤년입니다.")
    else:
        return HttpResponse("윤년이 아닙니다.")

# 3. http://127.0.0.1:8000/guestbook/calc/add/4/5 이면 더하기 연산결과
#    http://127.0.0.1:8000/guestbook/calc/sub/4/5 이면 빼기 연산결과
def calc(request, s, x, y):
    if s == "add":
        result = int(x) + int(y)
    elif s == "sub":
        result = int(x) - int(y)
    else:
        result = "지원 안함"
    return HttpResponse(result)


# 디비 연결 안 돼서 간단하게 list로 데이터 전달하기
flowers = ["작약", "목단", "이팝나무", "장미", "국화", "진달래", "철쭉"]

def list(request):
    # html 페이지와 결합하고 싶으면
    # /templates
    return render(request, "guestbook/guestbook_list.html",
                  {"title":"HTML 연동하기", "flowersList":flowers})

def write(request):
    # html 문서로 단순이동만
    return render(request, "guestbook/guestbook_write.html")

def save(request):
    flower = request.POST.get("flower")
    return HttpResponse(flower)

def add_write(request):
    return render(request, "guestbook/guestbook_addWirte.html")

def add_save(request):
    x = int(request.POST.get("x"))
    y = int(request.POST.get("y"))
    operator = request.POST.get("operator")
    result = 0
    if operator == "1":
        result = x + y
        operator = "+"
    elif operator == "2":
        result = x - y
        operator = "-"
    elif operator == "3":
        result = x * y
        operator = "*"
    elif operator == "4":
        result = x / y
        operator = "/"
    else:
        return HttpResponse("오류")
    
    return HttpResponse(f"{x} {operator} {y} = {result}")
    
# 데이터를 주는 경우
def getData(request):
    # json_dumps_params={'ensure_ascii':False} << 한글깨짐문제 해결
    return JsonResponse({"name":"홍길동", "age":23, "phone":"010-0000-0001"},
                        json_dumps_params={'ensure_ascii':False})

def userInfo(request):
    return render(request, "guestbook/userInfo.html")


