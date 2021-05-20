import django_filters.rest_framework
from rest_framework import (filters, generics, permissions, response, status,
                            viewsets)

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
        post = generics.get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments

    def perform_create(self, serializer):
        post = generics.get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)


class GroupAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowAPIView(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('user__username',)

    def get_queryset(self, *args, **kwargs):
        return self.request.user.following

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        following = generics.get_object_or_404(
            User,
            username=serializer.validated_data["following"]["username"]
        )
        if following != self.request.user:
            if not self.request.user.follower.filter(
                following=following,
            ).exists():
                serializer.save(user=self.request.user, following=following)
                return response.Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
        return response.Response(status=status.HTTP_400_BAD_REQUEST)
