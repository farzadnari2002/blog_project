from django.urls import path
from .views import *


app_name = 'blog_app'

urlpatterns = [
    path('detail/<slug:slug>', article_detail, name='article_detail'),
    path('list', ArticleList.as_view(), name='article_list'),
    path('category/<int:pk>', category_detail, name='category_detail'),
    path('search', search, name='search'),
    path('like/<slug:slug>/<int:pk>', like, name='like'),
]
