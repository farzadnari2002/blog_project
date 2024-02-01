from django.shortcuts import render
from .models import Article



def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog_app/article_detail.html', context={'article':article})
    
    

