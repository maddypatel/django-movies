from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Movie, Rating
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
    movies = Movie.object.all()
    template = loader.get_template('movies/allmovies.html')
    context = RequestContext(request, {
        'movies': movies,
    })
    return HttpResponse(template.render(context))