from django import forms
from django.core.exceptions import ValidationError
from .models import Comment



class ContactUsForm(forms.Form):
    years = ['2020', '2021', '2023']
    FAVORITE_COLORS_CHOICES = [
    ("blue","Blue"),
    ("green", "Green"),
    ("black", "Black"),
    ]
    name = forms.CharField(label='your name', max_length=10)
    message = forms.CharField(label='your message', max_length=10)
    data = forms.DateField(label='your date', widget=forms.SelectDateWidget(years=years, attrs={'class':'form-control'}))
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    
    
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
        
        
        