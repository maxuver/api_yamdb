from django_filters import rest_framework as filt
from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from reviews.models import Category, Genre, Title

from .filters import TitleFilter
from .mixins import ListCreateDeleteViewSet
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleReadSerializer, TitleWriteSerializer)


class TitleViewsSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    read_serializer_class = TitleReadSerializer
    write_serializer_class = TitleWriteSerializer
    filter_backends = [filt.DjangoFilterBackend]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'get'):
            return self.read_serializer_class
        return self.write_serializer_class

    def get_permissions(self):
        if self.action in ('get', 'list'):
            return AllowAny(),
        if self.action in ('destroy', 'create', 'update'):
            return IsAdminUser(),
        return {}


class GenreViewsSet(ListCreateDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            return AllowAny(),
        if self.action in ('destroy', 'create'):
            return IsAdminUser(),
        return {}


class CategoryViewsSet(ListCreateDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            return AllowAny(),
        if self.action in ('destroy', 'create'):
            return IsAdminUser(),
        return {}
