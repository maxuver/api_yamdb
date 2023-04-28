from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                       ReviewViewSet, CommentViewSet)
from api.views import (UsersViewSet, user_create_view,
                       user_jwt_token_create_view)

v1_router = routers.DefaultRouter()
v1_router.register('users', UsersViewSet, basename='users')
v1_router.register('categories', CategoryViewSet,
                          basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
                          ReviewViewSet, basename='reviews')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews'
                          r'/(?P<review_id>\d+)/comments',
                          CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', user_create_view),
    path('v1/auth/token/', user_jwt_token_create_view)
]
