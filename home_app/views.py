from django.shortcuts import render
from blog_app.models import Article


def home(request):
    articles = Article.objects.filter(status=True)
    # articles = Article.objects.all()

    return render(request, 'home_app/index.html', context={'articles': articles})



