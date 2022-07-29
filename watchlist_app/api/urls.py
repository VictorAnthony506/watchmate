from os import name
from django import views
from django.urls import path, include
from .views import MovieListAv, MovieDetailAv
# from watchlist_app.api.views import movie_details, movie_list, movie_details

urlpatterns = [    
    path('list/', MovieListAv.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailAv.as_view(), name='movie-detail')
]

