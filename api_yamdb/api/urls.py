from django.urls import include, path
from rest_framework import routers


from api.views import (user_create_view,
                       user_jwt_token_create_view)

v1_router = routers.DefaultRouter()


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', user_create_view),
    path('v1/auth/token/', user_jwt_token_create_view)
]
