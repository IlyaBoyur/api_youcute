from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet


router_v1 = DefaultRouter()
router_v1.register('v1/posts',
                   PostViewSet,
                   basename='posts')
urlpatterns = [
    path('v1/token/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router_v1.urls)),
]
