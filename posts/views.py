from datetime import datetime

from django.http.response import HttpResponse

from posts.models import Post

# Create your views here.


def hello(r):
    return HttpResponse("Hello <h1>world!</h1>")


def name(r):
    name = "Sara"
    return HttpResponse(f"Hello <h1>{name}</h1>")


def time(r):
    dt = datetime.now()

    return HttpResponse(f"NOW: {dt.strftime('%d-%m-%Y %H:%M:%S')}")

from django.http import HttpResponse

def student(request):
    return HttpResponse("Я студент")