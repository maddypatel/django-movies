from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from .models import Movie, Rating, Rater
from django.db.models import Avg
from movies.forms import UserForm

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request,
                  "movies/allmovies.html",
                  {"m": movies})


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
    ratings = movie.rating_set.all()
    template = loader.get_template('movies/movie.html')
    context = RequestContext(request, {
        'movie': movie,
        'ratings': ratings,
    })
    return HttpResponse(template.render(context))


def rater(request, rater_id):
    rater = Rater.objects.get(pk = rater_id)
    ratings = rater.rating_set.all()
    #not_rated = Movie.objects.filter(rating__rater__movie = request.movie.title)
    template = loader.get_template('movies/rater.html')
    context = RequestContext(request, {
        'rater': rater,
        'ratings': ratings,
    })
    return HttpResponse(template.render(context))


def user_register(request):
    if request.method == "GET":
        user_form = UserForm()
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            password = user.password
            user.set_password(password)
            user.save()
            user = authenticate(username = user.username,
                                password = password)
            login(request, user)

            return redirect('index')
    return render(request, "movies/register.html",
                  {'user_form': user_form})
