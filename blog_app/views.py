from django.shortcuts import render
from .models import Article, Category, Comment
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import ContactUsForm




def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(article=article, user=request.user, body=body, parent_id=parent_id)
    return render(request, 'blog_app/article_detail.html', context={'article':article})


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    objects_list = paginator.page(page_number)
    return render(request, 'blog_app/article_list.html', context={'articles':objects_list})


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


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['massage'])
            return redirect('home_app:home')
    form = ContactUsForm()
    return render(request, 'blog_app/contact_us.html', context={'form':form})
    
    

