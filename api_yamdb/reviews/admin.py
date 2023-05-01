from django.contrib import admin

from .models import Review, Title


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'score', 'pub_date')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'rating', 'description', 'genre', 'category')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Title, TitleAdmin)
