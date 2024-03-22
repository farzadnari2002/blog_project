from django import forms
from django.core.exceptions import ValidationError
from .models import Comment

         
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('parent', 'body')
        labels = {
            "body":'',
        }
        widgets = {
            'parent': forms.TextInput(attrs={
                'class': 'col-md-12 col-sm-12',
                'name':'parent_id',
                'type':'hidden',
                'id': 'parent_id',
                'placeholder': 'reply to'
            }),
            'body': forms.Textarea(attrs={
                'class': 'col-lg-12',
                'name': 'body',
                'rows': '6',
                'id': "body",
                'placeholder': "Type your comment",
                'required': "",
                 
            })
        }
        
        
        