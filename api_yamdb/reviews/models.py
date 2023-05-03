from django.db import models
from .validators import validate_actual_year


class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=256, verbose_name='название')
    year = models.IntegerField(
        verbose_name='год создания',
        validators=[validate_actual_year])
    rating = models.IntegerField(verbose_name='рейтинг', default=5)
    description = models.TextField(verbose_name='описание')
    genre = models.ManyToManyField(Genre, through='GenreTitle')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category'], name='unique_name_category'
            ),
        ]

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'
