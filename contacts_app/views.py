from django.shortcuts import render
from django.views.generic import CreateView
from .models import Message


class MessageCreate(CreateView):
    model = Message
    fields = ('__all__')
    success_url = '/'
    