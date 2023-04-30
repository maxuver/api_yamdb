from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from reviews.models import Category, Genre, Title
from .permissions import IsAdminOrReadOnly
from .filters import TitleFilter
from .mixins import ListCreateDeleteViewSet
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleReadSerializer, TitleWriteSerializer)


class TitleViewsSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    read_serializer_class = TitleReadSerializer
    write_serializer_class = TitleWriteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ('list', 'get'):
            return self.read_serializer_class
        return self.write_serializer_class


class GenreViewsSet(ListCreateDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewsSet(ListCreateDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
