from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from posts import views
from posts.views import create_post, delete_post, edit_post, post_detail, post_list, my_posts
from user.views import register


urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register", register, name="register"),
    path("path", views.hello),
    path("name", views.name),
    path("now", views.time),
    path("student/", views.student),

    path("", views.post_list, name="post_list"),
    path("post/create/", views.create_post, name="create_post"),
    path("posts/my/", my_posts, name="my_posts"),
    path("post/<int:pk>/edit", edit_post, name="edit_post"),
    path("post/<int:pk>/delete", delete_post, name="delete_post"),
    path("post/<int:pk>", views.post_detail, name="post_detail"),
    path("posts/active/", views.active_post_list, name="active_post_list"),

    path(
        "post/<int:pk>/toggle-active/",
        views.toggle_post_active,
        name="toggle_post_active",
    ),
    path(
    "category/create/",
    views.create_category,
    name="create_category",
),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )