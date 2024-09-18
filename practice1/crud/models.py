from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    published_date=models.DateField()
    is_available=models.BooleanField(default=True)
    