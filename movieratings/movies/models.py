from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    zip_code = models.CharField(max_length=10)
    user = models.OneToOneField(User, null=True)

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

def create_user():
    for rater in Rater.objects.all():
        user = User.objects.create_user(
            "user{}".format(rater.id),
            "user{}@theironyard.com".format(rater.id),
            "user{}".format(rater.id)
        )
        rater.user = user
        rater.save()
