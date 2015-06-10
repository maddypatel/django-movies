from django.contrib import admin
from .models import Rater, Movies, Ratings

# Register your models here.

admin.site.register(Rater)
admin.site.register(Movies)
admin.site.register(Ratings)
