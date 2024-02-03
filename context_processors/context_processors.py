from blog_app.models import Article
from django.shortcuts import render



def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')[0:3]
    return render(request, )