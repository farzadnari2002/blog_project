from django.shortcuts import render
from blog_app.models import Article



def home(request):
    articles = Article.objects.filter(status=True)
    # articles = Article.objects.all()
    # article = Article.objects.get(title="python")
    # print(f"ala {article.body}")
    qtest = Article.objects.filter(title="python")
    print(qtest)

    return render(request, 'home_app/index.html', context={'articles': articles})
