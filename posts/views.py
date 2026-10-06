from datetime import datetime

from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render

from posts.models import Post

# Create your views here.
posts = Post.objects.filter(is_active=True)

def hello(r):
    return HttpResponse("Hello <h1>world!</h1>")


def name(r):
    post = Post.objects.filter(id=2).first()

    if post is None:
        return HttpResponse("Пост с id=2 не найден")

    return HttpResponse(
        f"Название: {post.title}\n"
        f"Описание: {post.description}\n"
        f"Активен: {post.is_active}",
        content_type="text/plain; charset=utf-8",
    )

# Create your views here.
def post_list(request: HttpRequest):
    posts = Post.objects.all()  # SELECT * FROM posts;
    print(request.path)
    return render(request, "posts/list.html", context={"posts": posts})


def time(r):
    dt = datetime.now()

    return HttpResponse(f"NOW: {dt.strftime('%d-%m-%Y %H:%M:%S')}")

def student(request):
    return HttpResponse("Я студент")

def post_detail(r, pk):
    post = Post.objects.get(id=pk)  # SELECT * FROM posts WHERE id = ?;
    print(r.path)
    return render(r, "posts/detail.html", context={"post": post})
def active_post_list(request: HttpRequest):
    posts = Post.objects.filter(is_active=True)
    print(request.path)

    return render(
        request,
        "posts/active_list.html",
        context={"posts": posts}
    )

