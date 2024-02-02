from django.shortcuts import render
from blog_app.models import Article
from django.urls import reverse



def home(request):
    articles = Article.objects.filter(status=True)
    # articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('-created')[0:3]

    return render(request, 'home_app/index.html', context={'articles': articles, "recent_articles":recent_articles})
