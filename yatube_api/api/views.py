from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import permissions

from api.permissions import AuthorReadOnly
from api.serializer import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, AuthorReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, AuthorReadOnly,)

    def get_post_id(self):
        return self.kwargs.get('post_id')

    def get_post(self):
        return get_object_or_404(Post, id=self.get_post_id())

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            post=self.get_post(),
            author=self.request.user
        )
