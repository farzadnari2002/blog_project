from django.shortcuts import render
from .models import Article
from django.urls import reverse
from django.shortcuts import get_object_or_404



def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog_app/article_detail.html', context={'article':article})
    
    

