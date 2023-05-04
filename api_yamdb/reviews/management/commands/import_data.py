import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import Category, Genre, Title, GenreTitle, Comment, Review
from users.models import User


class Command(BaseCommand):
    help = 'Import data from csv files'

    def handle(self, *args, **options):
        csv_files = {
            'users.csv': User,
            'category.csv': Category,
            'genre.csv': Genre,
            'titles.csv': Title,
            'genre_title.csv': GenreTitle,
            'review.csv': Review,
            'comments.csv': Comment
        }

        for csv_file, model in csv_files.items():
            with open(os.path.join(
                    settings.BASE_DIR,
                    'static/data/',
                    csv_file),
                    encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    model.objects.create(**row)

            self.stdout.write(self.style.SUCCESS(
                f'{model.__name__} data imported successfully from {csv_file}'))
