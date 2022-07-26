from os import name
from django.urls import path, include
from watchlist_app.views import movie_details, movie_list, movie_details

urlpatterns = [    
    path('list/', movie_list, name='movie-list'),
    path('<int:pk>', movie_details, name='movie-detail')
]

