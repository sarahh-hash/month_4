from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("path", views.hello),
    path("name", views.name),
    path("now", views.time),
    path("student/", views.student),

    path("", views.post_list, name="post_list"),
    path("post/create/", views.create_post, name="create_post"),
    path("post/<int:pk>", views.post_detail, name="post_detail"),
    path("posts/active/", views.active_post_list, name="active_post_list"),

    path(
        "post/<int:pk>/toggle-active/",
        views.toggle_post_active,
        name="toggle_post_active",
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