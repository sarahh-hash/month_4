from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from posts.forms import CategoryForm, PostForm
from posts.models import Post


def hello(request):
    return HttpResponse("Hello <h1>world!</h1>")


def name(request):
    post = Post.objects.filter(id=2).first()

    if post is None:
        return HttpResponse("Пост с id=2 не найден")

    return HttpResponse(
        f"Название: {post.title}\n"
        f"Описание: {post.description}\n"
        f"Активен: {post.is_active}",
        content_type="text/plain; charset=utf-8",
    )


def time(request):
    dt = datetime.now()
    return HttpResponse(f"NOW: {dt.strftime('%d-%m-%Y %H:%M:%S')}")


def student(request):
    return HttpResponse("Я студент")


def post_list(request: HttpRequest):
    posts = Post.objects.order_by("-created_at", "-id")

    if search := request.GET.get("search"):
        posts = posts.filter(description__icontains=search)

    return render(request, "posts/list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/detail.html", {"post": post})


def active_post_list(request: HttpRequest):
    posts = Post.objects.filter(
        is_active=True
    ).order_by("-created_at", "-id")

    return render(request, "posts/active_list.html", {"posts": posts})


@login_required
def my_posts(request: HttpRequest):
    posts = Post.objects.filter(
        author=request.user
    ).order_by("-created_at", "-id")

    # Используем уже существующий шаблон списка
    return render(request, "posts/list.html", {"posts": posts})


@login_required
def create_post(request: HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_detail", post.pk)
    else:
        form = PostForm()

    return render(request, "posts/create.html", {"form": form})


@login_required
def edit_post(request: HttpRequest, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("post_detail", post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "posts/create.html", {"form": form})


@login_required
def delete_post(request: HttpRequest, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        return redirect("my_posts")

    return render(request, "posts/delete.html", {"post": post})


def create_category(request: HttpRequest):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("create_post")
    else:
        form = CategoryForm()

    return render(
        request,
        "posts/create_category.html",
        {"form": form},
    )


@require_POST
def toggle_post_active(request: HttpRequest, pk):
    post = get_object_or_404(Post, pk=pk)
    post.is_active = not post.is_active
    post.save(update_fields=["is_active"])

    return redirect("post_detail", post.pk)