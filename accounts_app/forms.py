from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'wrap-input100 validate-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))