from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Movie, Rating, Rater
from django.db.models import Avg

# Create your views here.

def topmovies(request):
    top_20_movies = Movie.objects.annotate(average = Avg('rating__rating')).order_by('-average')
    template = loader.get_template('movies/topmovies.html')
    context = RequestContext(request, {
        'top_20_movies': top_20_movies[:20],
    })
    return HttpResponse(template.render(context))

def allmovies(request):
    movies = Movie.objects.all()
    template = loader.get_template('movies/allmovies.html')
    context = RequestContext(request, {
        'movies': movies,
    })
    return HttpResponse(template.render(context))

def allraters(request):
    raters = Rater.objects.all()
    template = loader.get_template('movies/allraters.html')
    context = RequestContext(request, {
        'raters': raters,
    })
    return HttpResponse(template.render(context))

def movie(request, movie_id):
    movie = Movie.objects.get(pk = movie_id)
    template = loader.get_template('movies/movie.html')
    context = RequestContext(request, {
        'movie': movie,
    })
    return HttpResponse(template.render(context))

def rater(request, rater_id):
    rater = Rater.objects.get(pk = rater_id)
    template = loader.get_template('movies/rater.html')
    context = RequestContext(request, {
        'rater': rater,
    })
    return HttpResponse(template.render(context))