from django.urls import path
from .views import *


app_name = 'blog_app'

urlpatterns = [
    path('detail/<slug:slug>', article_detail, name='article_detail'),
    path('list', ArticleList.as_view(), name='article_list'),
    path('category/<int:pk>', category_detail, name='category_detail'),
    path('search', search, name='search'),
    path('contactus', contact_us, name='contact_us'),
    path('test1', TestBaseView.as_view(), name='test1'),
    path('test2', TestBaseView2.as_view(), name='test2'),
    path('red', Redirect.as_view(), name='red'),
]
