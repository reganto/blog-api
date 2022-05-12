from django.urls import path
from api.v1 import views

app_name = "v1"

urlpatterns = [
    path(
        "posts/",
        views.post_list,
        name="post_list",
    ),
    path(
        "posts/<int:pk>/",
        views.post_detail,
        name="post_detail",
    ),
    path(
        "posts/<int:post_pk>/comments/",
        views.comment_list,
        name="comment_list",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:comment_pk>/",
        views.comment_detail,
        name="comment_detail",
    ),
]
