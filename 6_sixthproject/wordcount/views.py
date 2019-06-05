from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

# render 세개의 인자 가능 -> request, html 파일, 사전형 객체 받아들일 수 있음
