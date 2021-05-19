import django_filters.rest_framework
from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly,)
    filter_backends=[django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields=['group',]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# TODO:  Напишите свой вариант
