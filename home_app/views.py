from django.shortcuts import render
from blog_app.models import Article, Testforsave



def home(request):
    articles = Article.objects.filter(status=True)
    # articles = Article.objects.all()
    testi = Testforsave(title="yek1", desc='do2')
    testi.save()

    
    return render(request, 'home_app/index.html', context={'articles': articles})
