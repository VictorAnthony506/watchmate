# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = list(movies.values())
    
#     return JsonResponse({'movie': data})
    
# def movie_details(request, pk):
#     """Function to extract individual information from result of movie_list function"""
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
#     return JsonResponse(data)
    