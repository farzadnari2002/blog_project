from django.urls import path
from .views import *


app_name = 'blog_app'

urlpatterns = [
    path('detail/<slug:slug>', ArticleDetail.as_view(), name='article_detail'),
    path('list', ArticleList.as_view(), name='article_list'),
    path('category/<int:pk>', category_detail, name='category_detail'),
    path('search', search, name='search'),
    path('contactus', MessageCreate.as_view(), name='contact_us'),
    path('test1', TestBaseView.as_view(), name='test1'),
    path('test2', TestBaseView2.as_view(), name='test2'),
    path('messages', MessageList.as_view(), name='message_list'),
    path('message/edit/<int:pk>', MessageUpdate.as_view(), name='message_edit'),
    path('message/delete/<int:pk>', MessageDelete.as_view(), name='message_delete'),
    path('archive/', ArticleArchiveIndexView.as_view(), name='article_archive'),
]
