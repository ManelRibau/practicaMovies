from django.shortcuts import render

def movie_list(request):
    return render(request, 'movie/movie_list.html', {})