import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from reviews.models import Category, Genre, Title, GenreTitle, Comment, Review
from users.models import User


class Command(BaseCommand):
    help = 'Import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        parser.add_argument('model', type=str)

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        model = options['model']
        if model == 'user':
            with open(os.path.join(
                    settings.BASE_DIR, 'static/data/', csv_file_path)
                    ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    User.objects.create(
                        username=row['username'],
                        email=row['email'],
                        role=row['role'],
                        bio=row['bio'],
                        first_name=row['first_name'],
                        last_name=row['last_name']
                    )
            self.stdout.write(self.style.SUCCESS(
                'User data imported successfully'))
        elif model == 'Category':
            with open(os.path.join(
                    settings.BASE_DIR, 'static/data/', csv_file_path)
                    ) as csvfile:
                reader = csv.DictReader(csvfile)
                #  next(reader)  # пропускаем первую строку
                for row in reader:
                    Category.objects.create(
                        name=row['name'],
                        slug=row['slug'],
                    )
            self.stdout.write(self.style.SUCCESS(
                'Category data imported successfully'))
        elif model == 'Genre':
            with open(os.path.join(
                    settings.BASE_DIR, 'static/data/', csv_file_path)
                    ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Genre.objects.create(
                        name=row['name'],
                        slug=row['slug'],
                    )
            self.stdout.write(self.style.SUCCESS(
                'Genre data imported successfully'))
        elif model == 'Title':
            with open(os.path.join(
                    settings.BASE_DIR, 'static/data/', csv_file_path)
                    ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Title.objects.create(
                        name=row['name'],
                        year=row['year'],
                        category=row['category']
                    )
            self.stdout.write(self.style.SUCCESS(
                'Title data imported successfully'))
        elif model == 'GenreTitle':
            with open(os.path.join(
                    settings.BASE_DIR, 'static/data/', csv_file_path)
                    ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    GenreTitle.objects.create(
                        title_id=row['title_id'],
                        genre_id=row['genre_id'],
                    )
            self.stdout.write(self.style.SUCCESS(
                'GenreTitle data imported successfully'))
        elif model == 'Review':
            with open(os.path.join(
                    settings.BASE_DIR, 'static/data/', csv_file_path)
                    ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Review.objects.create(
                        title_id=row['title_id'],
                        text=row['text'],
                        author=row['author'],
                        score=row['score'],
                        pub_date=row['pub_date']
                    )
            self.stdout.write(self.style.SUCCESS(
                'Review data imported successfully'))
        elif model == 'Comment':
            with open(os.path.join(
                    settings.BASE_DIR, 'static/data/', csv_file_path)
                    ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Comment.objects.create(
                        review_id=row['review_id'],
                        text=row['text'],
                        author=row['author'],
                        pub_date=row['pub_date'],
                    )
            self.stdout.write(self.style.SUCCESS(
                'Comment data imported successfully'))
        else:
            self.stdout.write(self.style.ERROR('Invalid model name'))
