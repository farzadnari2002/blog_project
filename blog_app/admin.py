from typing import Any
from django.contrib import admin
from .models import *


class FilterByTitle(admin.SimpleListFilter):
    title = 'کلیدهای پرتکرار'
    parameter_name = 'title'
    
    def lookups(self, request, model_admin):
        return (
            ('django', 'DJANGO'),
            ('yek', 'YEK'),
        )
        
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())
        
        
class CommentInline(admin.TabularInline):
    model = Comment
                


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'show_image', 'status',)
    list_filter = ('status', 'category', FilterByTitle)
    search_fields = ('title',)
    list_editable = ('status',)
    inlines = (CommentInline,)
    
    
    @admin.register(SocialMedia)
    class SOcialMediaAdmin(admin.ModelAdmin):
        list_display = ('instagram', 'telegram', 'whatsapp')

    
    
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Message)
admin.site.register(Like)



