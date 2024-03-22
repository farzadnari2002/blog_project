from django.contrib import admin
from .models import Message, SocialMedia


@admin.register(SocialMedia)
class SOcialMediaAdmin(admin.ModelAdmin):
    list_display = ('instagram', 'telegram', 'whatsapp')
    
    
admin.site.register(Message)

