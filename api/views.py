import django_filters.rest_framework
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.generics import get_object_or_404

from .exceptions import BadRequestAPIException
from .models import Group, Post, User
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('group',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)

    def get_queryset(self, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)


class GroupAPIView(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowAPIView(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('user__username',)

    def get_queryset(self, *args, **kwargs):
        return self.request.user.following

    def perform_create(self, serializer):
        following = get_object_or_404(
            User,
            username=serializer.validated_data["following"].username
        )
        if (following == self.request.user
           or self.request.user.follower.filter(following=following).exists()):
            raise BadRequestAPIException()
        serializer.save(user=self.request.user)
