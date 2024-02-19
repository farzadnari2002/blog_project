from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))
    
    
    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise ValidationError('username or password is wrong', code='invalid_info')
        