from django.contrib import admin
from .models import Message, Contact


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('instagram', 'telegram', 'whatsapp')
    
    
admin.site.register(Message)

