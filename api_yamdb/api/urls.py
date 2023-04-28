from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TitleViewsSet, GenreViewsSet, CategoryViewsSet

v1_router = DefaultRouter()

v1_router.register('titles', TitleViewsSet)
v1_router.register('genres', GenreViewsSet)
v1_router.register('categories', CategoryViewsSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
