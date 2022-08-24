from asyncio import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics, mixins
from watchlist_app.models import Review, StreamPlatform, WatchList
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from .serializers import (ReviewSeriaizer, 
                          WatchListSerializer, 
                          StreamPlatformSerializer)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSeriaizer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        return Review.objects.all()
    
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk) 
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=movie, review_user=review_user)  
          
        if review_queryset.exists():
            raise ValidationError(" You have already reviewed this movie! ")
        
        if movie.number_rating == 0:
            movie.avg_rating = serializer.validated_data['rating']
        else:
            movie.avg_rating = (movie.avg_rating + serializer.validated_data['rating'])/2
            
        movie.number_rating = movie.number_rating + 1  
        movie.save()    
        serializer.save(watchlist=movie, review_user=review_user)
        

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSeriaizer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSeriaizer
    permission_classes = {IsReviewUserOrReadOnly}
    
    
    
# class ReviewList(mixins.ListModelMixin,
#                  mixins.CreateModelMixin,
#                  generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSeriaizer
    
    
#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
    
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSeriaizer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    

class StreamPlatformAv(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    
    def get(self, request):
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class StreamPlatformDetailAv(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    
    def get(self, request, pk):
        
        if request.method == 'GET':
            try:            
                platform = StreamPlatform.objects.get(pk=pk)
            except StreamPlatform.DoesNotExist:
                return Response({'Error': 'platform Not Found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = StreamPlatformSerializer(platform)
            return Response(serializer.data)
        
        
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
class WatchListAv(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

    
        
class WatchDetailAv (APIView):
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk):
        if request.method == 'GET':
            try:            
                movies = WatchList.objects.get(pk=pk)
            except WatchList.DoesNotExist:
                return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = WatchListSerializer(movies)
            return Response(serializer.data)
        
    def put(self, request, pk):
        movies = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        movies = WatchList.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
           

    
        


"""Using Function based view"""
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':        
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:            
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         else:
#             return Response(serializer.errors)
        
    
#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete
#         return Response(status=status.HTTP_204_NO_CONTENT)