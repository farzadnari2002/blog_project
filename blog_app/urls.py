from django.urls import path
from .views import *


app_name = 'blog_app'

urlpatterns = [
    path('detail/<slug:slug>', article_detail, name='article_detail'),
    path('list', article_list, name='article_list'),
    path('category/<int:pk>', category_detail, name='category_detail'),
    path('search', search, name='search'),
    path('contactus', contact_us, name='contact_us'),
]
