from django.urls import path
from .views import MessageCreate


app_name = 'contacts_app'


urlpatterns = [
    path('messege', MessageCreate.as_view(), name='message')
]