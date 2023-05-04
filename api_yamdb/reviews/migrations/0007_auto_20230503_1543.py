# Generated by Django 3.2 on 2023-05-03 07:43

from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_remove_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(max_length=256, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[reviews.validators.validate_actual_year], verbose_name='год создания'),
        ),
    ]
