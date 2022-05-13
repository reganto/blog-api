from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v4.serializers import PostSerializer, CommentSerializer
from api.models import Post, Comment
from api.permissions import (
    IsStaffOrReadOnly,
    IsSuperUserOrAuthorOrReadOnly,
    IsSuperUserOrOwnerOrReadOnly,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
    serializer_class = CommentSerializer

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
