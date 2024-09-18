from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=224)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    avg_rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.title
    
    def update_rating(self, new_rating):
        self.rating += 1
        self.avg_rating = (self.avg_rating * (self.rating - 1) + new_rating) / self.rating
        self.save()
    
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    
    def __str__(self):
        return f"Review for {self.movie.title} on {self.create_date}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.movie.update_rating(self.rating)