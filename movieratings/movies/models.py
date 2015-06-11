from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return "Rater {}".format(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    def average_rating(self):
        return self.rating_set.all().aggregate(models.Avg('rating'))['rating__avg']


class Rating(models.Model):
    rating = models.IntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return "{} / {}".format(self.movie, self.rater)
