from typing import Any
from django.shortcuts import render, HttpResponse
from .models import Article, Category, Like
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import CommentForm
from django.views.generic.list import ListView
from django.http import JsonResponse


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if Like.objects.filter(user_id=request.user.id, article__slug=slug).exists():
        is_liked = True
    else:
        is_liked = False 
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.article_id = article.id
            form.user_id = request.user.id
            form.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'blog_app/article_detail.html', context={'article':article,'is_liked':is_liked, 'form':form})


def category_detail(request, pk):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'blog_app/article_list.html', context={'articles':articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    objects_list = paginator.page(page_number)
    return render(request, 'blog_app/article_list.html', context={'articles':objects_list})
    
    
class ArticleList(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 1
    
    
def like(request, slug, pk):
    try:
        like = Like.objects.get(user_id=request.user.id, article__slug=slug)
        like.delete()
        return JsonResponse({'response':'dislike'})
    except:
        Like.objects.create(user_id=request.user.id, article_id=pk )
        return JsonResponse({'response':'like'})




  


    

    
    
    

