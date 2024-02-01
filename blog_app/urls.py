from django.urls import path
from .views import *


app_name = 'blog_app'


urlpatterns = [
    path('detail/<int:id>',article_detail, name='article_detail')
]
