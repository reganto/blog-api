from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v4.serializers import PostSerializerDAB, CommentSerializerDAB
from api.models import Post, Comment
from api.permissions import (
    IsStaffOrReadOnly,
    IsSuperUserOrAuthorOrReadOnly,
    IsSuperUserOrOwnerOrReadOnly,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDAB
    search_fields = [
        "title",
        "body",
        "author__username",
    ]
    ordering_fields = ("created_at",)
    ordering = ("-created_at",)

    def get_permissions(self):
        permission_classes = [
            IsAuthenticated,
            IsStaffOrReadOnly,
        ]
        if self.action in [
            "update",
            "partial_update",
            "destroy",
        ]:
            permission_classes = [
                IsAuthenticated,
                IsSuperUserOrAuthorOrReadOnly,
            ]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializerDAB
    search_fields = [
        "body",
        "owner__username",
    ]
    ordering_fields = ("created_at",)
    ordering = ("-created_at",)

    def get_permissions(self):
        permission_classes = [
            IsAuthenticated,
            IsStaffOrReadOnly,
        ]
        if self.action in [
            "update",
            "partial_update",
            "destroy",
        ]:
            permission_classes = [
                IsAuthenticated,
                IsSuperUserOrOwnerOrReadOnly,
            ]
        return [permission() for permission in permission_classes]
