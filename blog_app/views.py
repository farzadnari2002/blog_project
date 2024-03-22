from typing import Any
from django.shortcuts import render, HttpResponse
from .models import Article, Category, Comment, Like
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from .forms import CommentForm
from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic import DetailView,FormView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import YearArchiveView, ArchiveIndexView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CustomLoginRequiredMixin
from django.http import JsonResponse
from django.views.generic.edit import FormMixin



def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.article_id = article.id
            form.user_id = request.user.id
            form.save()
    else:
        form = CommentForm()
    return render(request, 'blog_app/article_detail.html', context={'article':article, 'form':form})


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


# def contact_us(request):
#     if request.method == 'POST':
#         form = MessageForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#          form = MessageForm()          
#     return render(request, 'blog_app/contact_us.html', context={'form':form})


class TestBaseView(View):
    name = 'farzad'
    def get(self, request):
        return HttpResponse(self.name)
    
    
class TestBaseView2(TestBaseView):
    name = 'mamad'
    
    
# class ListView(View):
#     queryset = None
#     template_name = None
    
#     def get(self, request):
#         return render(request, self.template_name, context={'object_list':self.queryset})
    
    
class ArticleList(CustomLoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 1
 
    
    
class ArticleDetail(FormMixin, DetailView):
    model = Article
    form_class = CommentForm
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Like.objects.filter(user_id=self.request.user.id, article__slug=self.object.slug).exists():
            context['is_liked'] = True
        else:
            context['is_liked'] = False
        return context
    
    def form_valid(self, form):
        form_data = form.cleaned_data
        Comment.objects.create(**form_data)
        return super().form_valid(form)
               
    
# class ContactUs(FormView):
#     template_name = 'blog_app/contact_us.html'
#     form_class = MessageForm
#     success_url = '/'
    
    
#     def form_valid(self, form):
#         form_data = form.cleaned_data
#         Message.objects.create(**form_data)
#         return super().form_valid(form)
    
    
# class MessageCreate(CreateView):
#     model = Message
#     fields = ('__all__')
#     success_url = '/'
    
    
# class MessageList(ListView):
#     model = Message

    
# class MessageUpdate(UpdateView):
#     model = Message
#     fields = ('title', 'text')
#     template_name_suffix = '_update_form'
#     success_url = '/articles/messages'
    
    
# class MessageDelete(DeleteView):
#     model = Message
#     success_url = '/articles/messages'
    
    
class ArticleArchiveIndexView(ArchiveIndexView):
    model = Article
    date_field = 'created'
    
    
def like(request, slug, pk):
    try:
        like = Like.objects.get(user_id=request.user.id, article__slug=slug)
        like.delete()
        return JsonResponse({'response':'dislike'})
    except:
        Like.objects.create(user_id=request.user.id, article_id=pk )
        return JsonResponse({'response':'like'})




  


    

    
    
    

