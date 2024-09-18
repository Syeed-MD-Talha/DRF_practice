from django.db import models

# Create your models here.
class Todo(models.Model): 
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
    

class product(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    
    class Meta:
        db_table = 'Product'
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'