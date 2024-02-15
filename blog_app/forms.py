from django import forms



class ContactUsForm(forms.Form):
    massage = forms.CharField(label='your massage')