from pyexpat import model
from django.db import models
from tables import Description

# Create your models here.

# Many-to-many relationships
# Many-to-one relationships
# one-to-one relationships


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    def __str__(self):
        return self.name
    

class WatchList(models.Model):
    
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True) # if the movie is released or lauched for instance
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title



"""First Example Model Used"""
# class Movie(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     active = models.BooleanField(default=True)
    
#     def __str__(self):
#         return self.name

'''I deleted the data base (db.sqlite3) for a new model'''