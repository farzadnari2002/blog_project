from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'show_image')
    
    
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)


