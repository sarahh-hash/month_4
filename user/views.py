from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("my_posts")
    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form},
    )
    @login_required
    def my_posts(request):
        posts = Post.objects.filter(
            author=request.user
        ).order_by("-created_at", "-id")

        return render(request, "posts/my_posts.html", {"posts": posts})