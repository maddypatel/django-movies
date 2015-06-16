from django.contrib import admin
from .models import Rater, Movie, Rating, Genre

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields = ['title', 'genres']
    list_display = ['title', 'average_rating']

class GenreAdmin(admin.ModelAdmin):
    fields = ['genre']



admin.site.register(Rater)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)
admin.site.register(Genre, GenreAdmin)
