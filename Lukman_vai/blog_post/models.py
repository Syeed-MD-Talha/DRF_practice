from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    name=models.CharField(max_length=30)
    bio=models.TextField()
    phone_number=models.CharField(max_length=14)
    
    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class CategoryModel(models.Model):
    category_name=models.CharField(max_length=30)
    def __str__(self):
        return self.category_name
    
    class Meta:
        managed = True
        verbose_name_plural = 'Categories'
    

class PostModel(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    category=models.ManyToManyField(CategoryModel, blank=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        verbose_name_plural = 'Posts'
    


    
class ProfileModel(models.Model):
    name=models.CharField(max_length=20)
    about=models.TextField()
    author=models.OneToOneField(AuthorModel, on_delete=models.CASCADE)
    def __str__(self):
        return self.name   
    
    class Meta:
        managed = True
        verbose_name_plural = 'Profiles'

    

