from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import validate_username


class User(AbstractUser):

    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    USER_ROLES = (
        (ADMIN, 'Администратор'),
        (MODERATOR, 'Модератор'),
        (USER, 'Пользователь')
    )

    username = models.CharField(
        'имя пользователя',
        max_length=150,
        validators=[validate_username],
        unique=True
    )

    bio = models.TextField(
        'биография',
        blank=True,
    )
    email = models.EmailField(
        'email',
        unique=True,
        max_length=254,
    )
    first_name = models.CharField(
        'имя',
        max_length=150,
        blank=True
    )
    role = models.CharField('роль',
                            max_length=30,
                            choices=USER_ROLES,
                            default='user')

    class Meta:
        ordering = ('username',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == User.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == User.MODERATOR or self.is_staff
