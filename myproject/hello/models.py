from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    quantity = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    total_review = models.IntegerField(default=0)
    avg_rating = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField()
    book = models.ForeignKey(Book,related_name='reviews', on_delete=models.CASCADE)
    user_rating = models.FloatField()
    
    class Meta:
        unique_together = ('user', 'book')  # Ensures each user can only review a book once
    
    def __str__(self):
        return str(self.user)
    
    def save(self, *args, **kwargs):
        # Check if this is a new review by querying the database
        is_new = not Review.objects.filter(pk=self.pk).exists()
        
        print('is_new:', is_new)
        
        # Save the review
        super().save(*args, **kwargs)
        
        # If it's a new review, update the book's rating and review count
        if is_new:
            book = self.book
            book.total_review += 1
            book.avg_rating = ((book.avg_rating * (book.total_review - 1)) + self.user_rating) / book.total_review
            book.save()