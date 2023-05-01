from http import HTTPStatus
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from reviews.models import Category, Genre, Review, Title
from .permissions import IsAdminOrReadOnly
from .filters import TitleFilter
from .mixins import ListCreateDeleteViewSet
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleReadSerializer, TitleWriteSerializer,
                          ReviewSerializer)


from .permissions import (IsAdmin, IsAdminOrReadOnly,
                          IsOwnerAdminModeratorOrReadOnly)
from .serializers import (UsersSerializer, CreateUserSerializer,
                          UserJWTTokenCreateSerializer)
from users.models import User


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAdmin]
    serializer_class = UsersSerializer
    lookup_field = 'username'
    lookup_value_regex = '[^/]+'
    pagination_class = LimitOffsetPagination

    @action(methods=['patch', 'get'], detail=False,
            permission_classes=[permissions.IsAuthenticated],
            url_path='me', url_name='me')
    def me(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(
                instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=self.request.user.role)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_create_view(request):
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data.get('email')
    username = serializer.validated_data.get('username')
    serializer.save()
    confirmation_code = default_token_generator.make_token(
        User.objects.get(email=email, username=username)
    )
    MESSAGE = (f'Здравствуйте, {username}! '
               f'Ваш код подтверждения: {confirmation_code}')
    send_mail(message=MESSAGE,
              subject='Confirmation code',
              recipient_list=[email],
              from_email=None)
    return Response(serializer.data, status=HTTPStatus.OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_jwt_token_create_view(request):
    serializer = UserJWTTokenCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    confirmation_code = serializer.validated_data.get('confirmation_code')
    username = serializer.validated_data.get('username')
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, confirmation_code):
        token = AccessToken.for_user(user)
        return Response(
            data={'token': str(token)},
            status=HTTPStatus.OK
        )
    return Response(
        'Неверный код подтверждения или имя пользователя!',
        status=HTTPStatus.BAD_REQUEST
    )


class TitleViewSet(viewsets.ModelViewSet):
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


class GenreViewSet(ListCreateDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]


class CategoryViewSet(ListCreateDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (IsOwnerAdminModeratorOrReadOnly,)

    def get_title(self):
        return get_object_or_404(Title, id=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self.get_title().reviews.all()

    def perform_create(self, serializer):
            serializer.save(
                author=self.request.user,
                title=self.get_title()
            )
