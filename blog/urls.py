from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import register
from posts import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.PostListView.as_view(), name="post_list"),
    path("hello/", views.HelloView.as_view(), name="hello"),
    path("name/", views.NameView.as_view(), name="name"),
    path("time/", views.TimeView.as_view(), name="time"),
    path("student/", views.StudentView.as_view(), name="student"),

    path(
        "post/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    path(
        "posts/active/",
        views.ActivePostListView.as_view(),
        name="active_post_list",
    ),
    path(
        "posts/my/",
        views.MyPostsView.as_view(),
        name="my_posts",
    ),
    path(
        "post/create/",
        views.PostCreateView.as_view(),
        name="create_post",
    ),
    path(
        "post/<int:pk>/edit/",
        views.UpdatePostView.as_view(),
        name="edit_post",
    ),
    path(
        "post/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="delete_post",
    ),
    path(
        "category/create/",
        views.CategoryCreateView.as_view(),
        name="create_category",
    ),
    path(
        "post/<int:pk>/toggle/",
        views.TogglePostActiveView.as_view(),
        name="toggle_post_active",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("register/", register, name="register"),
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