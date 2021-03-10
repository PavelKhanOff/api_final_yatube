from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewsSet, PostViewsSet

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewsSet, basename='posts')
router_v1.register('group', GroupViewsSet, basename='groups')
router_v1.register('follow', FollowViewSet, basename='follows')
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router_v1.urls)),
]
