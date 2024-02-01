from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.utils import timezone



class Category(models.Model):
    title = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    category = models.ManyToManyField(Category)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now())
    status = models.BooleanField(default=False)
    
    
    

    def __str__(self):
        return f"{self.title} - {self.body[:30]}..."


 