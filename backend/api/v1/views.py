from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.v1.serializers import PostSerializer, CommentSerializer
from api.models import Post, Comment


@api_view(["GET", "POST"])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    elif request.method == "POST":
        serializer = PostSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )


@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "GET":
        serializer = PostSerializer(
            post,
            many=False,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    elif request.method == "PUT":
        serializer = PostSerializer(
            instance=post,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
    elif request.method == "DELETE":
        post.delete()
        return Response(
            {"message": "Post deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )


@api_view(["GET", "POST"])
def comment_list(request, post_pk):
    if request.method == "GET":
        comments = Comment.objects.filter(post_id=post_pk)
        serializer = CommentSerializer(
            comments,
            many=True,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    elif request.method == "POST":
        serializer = CommentSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )


@api_view(["GET", "PUT", "DELETE"])
def comment_detail(requset, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if requset.method == "GET":
        serializer = CommentSerializer(
            comment,
            many=False,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
    elif requset.method == "PUT":
        serializer = CommentSerializer(
            instance=comment,
            data=requset.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
    elif requset.method == "DELETE":
        comment.delete()
        return Response(
            {"message": "comment deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )
