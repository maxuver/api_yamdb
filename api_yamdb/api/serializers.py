from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404

from reviews.models import Category, Genre, Title, Review, Comment

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username', 'email')
        model = User


class UserJWTTokenCreateSerializer(serializers.Serializer):
    confirmation_code = serializers.CharField(required=True)
    username = serializers.CharField(required=True)


class CategorySerializer(serializers.ModelSerializer):

    ...


class GenreSerializer(serializers.ModelSerializer):

    ...


class TitlesReadSerializer(serializers.ModelSerializer):
    ...


class TitlesEditorSerializer(serializers.ModelSerializer):
    ...


class ReviewSerializer(serializers.ModelSerializer):
    ...


class CommentSerializer(serializers.ModelSerializer):
    ...