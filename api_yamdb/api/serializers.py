from django.contrib.auth import get_user_model
from rest_framework import serializers
from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    ...


class CreateUserSerializer(serializers.ModelSerializer):
    ...


class UserJWTTokenCreateSerializer(serializers.Serializer):
    ...
