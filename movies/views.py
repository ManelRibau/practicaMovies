from django.shortcuts import render
from django.utils import timezone
from .models import Movie

def movie_list(request):
    return render(request, 'movie/movie_list.html', {})

def movie_sci_fi(request):
    movies = Movie.objects.filter(genre__startswith='Ciencia')
    return render(request, 'movie/sci-fi.html', {'movies': movies})

def movie_action(request):
    movies = Movie.objects.filter(genre__startswith='Accio')
    return render(request, 'movie/action.html', {'movies': movies})

def movie_adventures(request):
    movies = Movie.objects.filter(genre__startswith='Aventur')
    return render(request, 'movie/adventures.html', {'movies': movies})

def movie_comedy(request):
    movies = Movie.objects.filter(genre__startswith='Comedia')
    return render(request, 'movie/comedy.html', {'movies': movies})

def movie_drama(request):
    movies = Movie.objects.filter(genre__startswith='Drama')
    return render(request, 'movie/drama.html', {'movies': movies})

def movie_romance(request):
    movies = Movie.objects.filter(genre__startswith='Romanti')
    return render(request, 'movie/romance.html', {'movies': movies})
