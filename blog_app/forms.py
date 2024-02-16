from django import forms



class ContactUsForm(forms.Form):
    name = forms.CharField(label='your name', max_length=10)
    massage = forms.CharField(label='your massage', max_length=10)