from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='Follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='CommentViewSet'
)

urlpatterns = [
    path('v1/', include(router.urls), name='api-root'),
    path('v1/', include('djoser.urls.jwt')),
]
