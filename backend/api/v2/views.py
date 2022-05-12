from rest_framework.response import Response
from rest_framework import status
from rest_framework import views

from api.models import Post, Comment
from api.v2.serializers import PostSerializer, CommentSerializer


class PostListView(views.APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        serializer = PostSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )


class PostDetailView(views.APIView):
    def initial(self, request, pk, *args, **kwargs):
        self.post = Post.objects.get(pk=pk)

    def get(self, request, pk):
        serializer = PostSerializer(
            self.post,
            many=False,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        serializer = PostSerializer(
            instance=self.post,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

    def delete(self, request, pk):
        self.post.delete()
        return Response(
            {"messate": "post deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )


class CommentListView(views.APIView):
    def get(self, request, post_pk):
        comments = Comment.objects.filter(post_id=post_pk)
        serializer = CommentSerializer(
            comments,
            many=True,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def post(self, request, post_pk):
        serializer = CommentSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )


class CommentDetailView(views.APIView):
    def initial(self, request, post_pk, comment_pk, *args, **kwargs):
        self.comment = Comment.objects.get(pk=comment_pk)

    def get(self, request, post_pk, comment_pk):
        serializer = CommentSerializer(
            self.comment,
            many=False,
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, post_pk, comment_pk):
        serializer = CommentSerializer(
            instance=self.comment,
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

    def delete(self, request, post_pk, comment_pk):
        self.comment.delete()
        return Response(
            {"message": "comment deleted"},
            status=status.HTTP_204_NO_CONTENT,
        )
