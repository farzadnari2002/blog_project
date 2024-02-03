from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify



class Category(models.Model):
    title = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)
    
    
    def get_absolute_url(self):
        return reverse('blog_app:category_detail', args=[self.id])
    
    
    
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
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    
    
    # class Meta:
    #     ordering = ('-created',)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args, kwargs)
        
    
    def get_absolute_url(self):
        return reverse('blog_app:article_detail', args=[self.slug])
    
    
    def __str__(self):
        return f"{self.title} - {self.body[:30]}..."


 