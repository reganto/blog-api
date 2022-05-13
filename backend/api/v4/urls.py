from rest_framework_nested import routers
from django.urls import include, path

from api.v4 import views

app_name = "v4"

router = routers.SimpleRouter()
router.register("posts", views.PostViewSet, basename="posts")
posts_router = routers.NestedSimpleRouter(router, "posts", lookup="post")
posts_router.register(
    "comments",
    views.CommentViewSet,
    basename="post-comments",
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]
