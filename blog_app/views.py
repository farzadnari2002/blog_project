from django.shortcuts import render
from .models import Article
from django.urls import reverse



def article_detail(request, id):
    article = Article.objects.get(id=id)
    print(reverse('blog_app:article_detail', args=[id]))
    return render(request, 'blog_app/article_detail.html', context={'article':article})
    
    

