from django.urls import path
from api.v3 import views

app_name = "v3"

urlpatterns = [
    path(
        "posts/",
        views.PostListView.as_view(),
        name="post_list",
    ),
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    path(
        "posts/<int:post_pk>/comments/",
        views.CommentListView.as_view(),
        name="comment_list",
    ),
    path(
        "posts/<int:post_pk>/comments/<int:id>/",
        views.CommentDetailView.as_view(),
        name="comment_detail",
    ),
]
