from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from posts.forms import CategoryForm, PostForm
from posts.models import Category, Post


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello <h1>world!</h1>")


class NameView(View):
    def get(self, request):
        post = Post.objects.filter(id=2).first()

        if post is None:
            return HttpResponse("Пост с id=2 не найден")

        return HttpResponse(
            f"Название: {post.title}\n"
            f"Описание: {post.description}\n"
            f"Активен: {post.is_active}",
            content_type="text/plain; charset=utf-8",
        )


class TimeView(View):
    def get(self, request):
        dt = datetime.now()
        return HttpResponse(
            f"NOW: {dt.strftime('%d-%m-%Y %H:%M:%S')}"
        )


class StudentView(View):
    def get(self, request):
        return HttpResponse("Я студент")


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        posts = Post.objects.order_by("-created_at", "-id")
        search = self.request.GET.get("search")

        if search:
            posts = posts.filter(description__icontains=search)

        return posts


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"
    pk_url_kwarg = "pk"


class ActivePostListView(ListView):
    model = Post
    template_name = "posts/active_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            is_active=True
        ).order_by("-created_at", "-id")


class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            author=self.request.user
        ).order_by("-created_at", "-id")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"pk": self.object.pk},
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/edit.html"
    context_object_name = "post"

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={"pk": self.object.pk},
        )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/delete.html"
    context_object_name = "post"
    success_url = reverse_lazy("my_posts")

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "posts/create_category.html"
    success_url = reverse_lazy("create_post")


class TogglePostActiveView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.is_active = not post.is_active
        post.save(update_fields=["is_active"])

        return redirect("post_detail", pk=post.pk)