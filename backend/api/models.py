from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    title = models.CharField(
        max_length=200,
    )
    body = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.title} by {self.author.username}"

    class Meta:
        ordering = ("-created_at",)


class Comment(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="comments",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    body = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.body[:50]} by {self.owner.username}"

    class Meta:
        ordering = ("-created_at",)
