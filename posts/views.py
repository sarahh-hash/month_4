from datetime import datetime

from django.http.response import HttpResponse

from posts.models import Post

# Create your views here.


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


def time(r):
    dt = datetime.now()

    return HttpResponse(f"NOW: {dt.strftime('%d-%m-%Y %H:%M:%S')}")

def student(request):
    return HttpResponse("Я студент")

