from django.shortcuts import render
from .models import Article, Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator



def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog_app/article_detail.html', context={'article':article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    
    if page_number :
        objects_list = paginator.page(page_number)

    else:
        objects_list = paginator.page(1)
    return render(request, 'blog_app/article_list.html', context={'articles':objects_list})


def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'blog_app/article_list.html', context={'articles':articles})
    
    

