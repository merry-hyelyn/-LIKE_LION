from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def home(request):
    blogs = Blog.objects  # 쿼리셋 : 객체들의 목록을 알 수 있음 # 메소드
    return render(request, 'home.html', {'blogs': blogs})
    # blogs 키값


# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(object).메소드


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog': blog_detail})


def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET["title"]
    blog.body = reqeust.GET["body"]
    blog.save()
