# Generated by Django 3.2 on 2023-05-02 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_review_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]
