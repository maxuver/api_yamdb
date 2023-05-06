from django.db import models

from .validators import validate_actual_year
from users.models import User


CHOICES = [(i, i) for i in range(1, 11)]


class BaseModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Genre(BaseModel):
    pass


class Category(BaseModel):
    pass


class Title(models.Model):
    name = models.CharField(max_length=256, verbose_name='название')
    year = models.IntegerField(
        verbose_name='год создания',
        validators=[validate_actual_year])
    description = models.TextField(verbose_name='описание', blank=True)
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


class Review(models.Model):
    text = models.TextField('текст отзыва')
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews',
        verbose_name='произведение')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews',
        verbose_name='автор')
    score = models.IntegerField('оценка', choices=CHOICES, default=10)
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='title_author_unique_match'
            ),
        ]

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):
    text = models.TextField('текст комментария')
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments',
        verbose_name='отзыв')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='автор')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:30]
