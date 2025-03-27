from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StreamPlatform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    platform_name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.platform_name
    
class Movie(models.Model):
    title = models.CharField(max_length=50)
    story_line = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.FloatField()
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.rating)