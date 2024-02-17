from django import forms
from django.core.exceptions import ValidationError



class ContactUsForm(forms.Form):
    years = ['2020', '2021', '2023']
    name = forms.CharField(label='your name', max_length=10)
    message = forms.CharField(label='your message', max_length=10)
    data = forms.DateField(label='your date', widget=forms.SelectDateWidget(years=years))
    
    
    def clean(self):
        name = self.cleaned_data.get('name')
        message = self.cleaned_data.get('message')
        if name == 'farzad':
            self.add_error('name', 'fazad nari cant send message')
        if name == message:
            raise ValidationError('name and message are same', code='name_message_same')
        
        
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if ' ' in name:
            raise ValidationError('no space in name',code='name_space_error')
        return name + ' test'
        