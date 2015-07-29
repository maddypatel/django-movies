"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from movies import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url('^index$', views.allmovies, name='index'),
    url(r'^topmovies$', views.topmovies, name='topmovies'),
    url(r'^allmovies$', views.allmovies, name='allmovies'),
    url(r'^allraters$', views.allraters, name='allraters'),
    url(r'^movie/(?P<movie_id>\d+)$', views.movie, name='movie'),
    url(r'^rater/(?P<rater_id>\d+)$', views.rater, name='rater'),
    url(r'^register$', views.user_register, name='user_register'),
    url(r'^rate/(?P<movie_id>\d*)$', views.rate_movie, name='rate_movie'),
    url(r'^edit_rating/(?P<movie_id>\d*)$', views.edit_rating, name='edit_rating'),
    url(r'^delete_rating/(?P<rating_id>\d*)$', views.delete_rating, name='delete_rating'),
]
