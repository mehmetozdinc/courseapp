from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=40)
    slug = models.CharField(default="",null=False,unique=True,db_index=True,max_length=50)

    def __str__(self):
        return f"{self.name}"
    
    



class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",blank=True,null=False, unique=True,db_index=True)
    categories = models.ManyToManyField(Category)



    def __str__(self):
        return f"{self.title}"
    



