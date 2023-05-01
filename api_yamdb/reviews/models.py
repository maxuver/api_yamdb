from django.db import models

from users.models import User

CHOICES = [(i,i) for i in range(1, 11)]


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    rating = models.IntegerField()
    description = models.TextField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name='genres',
        blank=True,
        null=True)
    category = models.ForeignKey(
        Category,
        unique=True,
        on_delete=models.SET_NULL,
        related_name='categories',
        blank=True,
        null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category'], name='unique_name_category'
            ),
        ]


class Review(models.Model):
    text = models.TextField()
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        choices=CHOICES,
        default=10
    )
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )

    def __str__(self):
        return self.text
