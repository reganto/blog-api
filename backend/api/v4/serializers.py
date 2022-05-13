from rest_framework import serializers

from api.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ("updated_at",)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("updated_at",)
