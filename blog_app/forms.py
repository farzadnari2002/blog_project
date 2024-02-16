from django import forms
from django.core.exceptions import ValidationError



class ContactUsForm(forms.Form):
    name = forms.CharField(label='your name', max_length=10)
    massage = forms.CharField(label='your message', max_length=10)
    
    
    def clean(self):
        name = self.cleaned_data.get('name')
        message = self.cleaned_data.get('message')
        if name == message:
            raise ValidationError