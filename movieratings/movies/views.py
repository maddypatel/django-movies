from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from .models import Movie, Rating, Rater
from django.db.models import Avg
from .forms import UserForm, RatingForm, EditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request,
                  "movies/allmovies.html",
                  {"m": movies})


def topmovies(request):
    top_20_movies = Movie.objects.annotate(average=Avg('rating__rating')).order_by('-average')
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
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    template = loader.get_template('movies/movie.html')
    context = RequestContext(request, {
        'movie': movie,
        'ratings': ratings,
    })
    return HttpResponse(template.render(context))


def rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all()
    movies = Movie.objects.all()
    rated = [rating.movie for rating in ratings]
    not_rated = [movie for movie in movies if movie not in rated]
    template = loader.get_template('movies/rater.html')
    context = RequestContext(request, {
        'rater': rater,
        'ratings': ratings,
        'not_rated': not_rated,
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
            user = authenticate(username=user.username,
                                password=password)
            login(request, user)

            return redirect('index')
    return render(request, "movies/register.html",
                  {'user_form': user_form})


@login_required
def rate_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if request.method == "POST":
        rating_form = RatingForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.rater = Rater.objects.get(id=request.user.id)
            rating.movie = movie
            rating.save()
            messages.add_message(request, messages.SUCCESS,
                                 "You have added the rating for {}.".format(rating.movie))

        return redirect('rater', request.user.id)
    else:
        rating_form = RatingForm()
    template = loader.get_template('movies/rate.html')
    context = RequestContext(request, {
        'rating_form': rating_form,
        'movie': movie
    })
    return HttpResponse(template.render(context))


@login_required
def edit_rating(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    current_rating = Rating.objects.get(rater__exact=request.user.id, movie__exact = movie_id)
    if request.method == "POST":
        edit_form = EditForm(request.POST, instance=current_rating)
        if edit_form.is_valid():
            new_rating = edit_form.save(commit=False)
            new_rating.rater = Rater.objects.get(id=request.user.id)
            new_rating.movie = movie
            new_rating.save()
            messages.add_message(request, messages.SUCCESS,
                                 "You have changed the rating of {}.".format(new_rating.movie))

        return redirect('rater', request.user.id)
    else:
        edit_form = EditForm(instance=current_rating)
    return render(request,
                  'movies/edit_rating.html',
                  {'edit_form': edit_form,
                   'movie': movie})


@login_required
def delete_rating(request, rating_id):
    rating = Rating.objects.get(pk=rating_id)
    if request.method == "POST":
        messages.add_message(request, messages.SUCCESS,
                             "You have deleted the rating for {}".format(rating.movie.title))
        rating.delete()
        return redirect('rater', request.user.id)
    return render(request, 'movies/delete.html', {"rating": rating})

