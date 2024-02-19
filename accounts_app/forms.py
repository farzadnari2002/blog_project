from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'input100'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))