from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zip_code = models.IntegerField()

    def __str__(self):
        return "{}".format(self.uid)


class Movies(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return "Title - {}, Genre - {}".format(self.title, self.genre)


class Ratings(models.Model):
    rating = models.IntegerField()
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movies)
