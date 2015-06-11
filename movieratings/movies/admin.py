from django.contrib import admin
from .models import Rater, Movie, Rating

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ['title', 'average_rating']

admin.site.register(Rater)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating)
