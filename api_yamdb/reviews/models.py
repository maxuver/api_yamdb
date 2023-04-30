from django.db import models

from .validators import validate_actual_year


class Title(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название'
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выпуска',
        validators=[validate_actual_year]
    )
