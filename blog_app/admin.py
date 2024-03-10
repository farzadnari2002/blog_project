from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'show_image', 'status',)
    list_filter = ('status', 'category')
    search_fields = ('title',)
    list_editable = ('status',)

    
    
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)


