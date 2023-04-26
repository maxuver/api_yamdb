from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ...

v1_router = DefaultRouter()

v1_router.register(...)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
