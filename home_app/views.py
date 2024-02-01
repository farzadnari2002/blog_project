from django.shortcuts import render
from blog_app.models import Article



def home(request):
    articles = Article.articles.filter(status=True)
    # articles = Article.objects.all()
    print(Article.articles.counter())

    return render(request, 'home_app/index.html', context={'articles': articles})
