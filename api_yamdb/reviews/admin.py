from django.contrib import admin

from .models import Category, Genre, GenreTitle, Review, Title


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'score', 'pub_date')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'rating', 'description', 'category')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')

class GenreTitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'genre', 'title')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
