from django.urls import include, path
from rest_framework import routers


from api.views import (UsersViewSet, user_create_view,
                       user_jwt_token_create_view)

v1_router = routers.DefaultRouter()
v1_router.register('users', UsersViewSet, basename='users')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', user_create_view),
    path('v1/auth/token/', user_jwt_token_create_view)
]
