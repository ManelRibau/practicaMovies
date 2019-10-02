from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('sci-fi/', views.movie_sci_fi, name='sci-fi'),
    path('action/', views.movie_action, name='action'),
    path('adventures/', views.movie_adventures, name='adventures'),
    path('drama/', views.movie_drama, name='drama'),
    path('romance/', views.movie_romance, name='romance'),
    path('comedy/', views.movie_comedy, name='comedy'),
]