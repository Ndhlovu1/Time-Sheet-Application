from django import forms
from .models import Comment

# Form - Allows you to build standard forms
# ModelForm - Allows you to build forms tied to model instances
# https://docs.djangoproject.com/en/3.0/ref/forms/fields/

class EmailPostForm(forms.Form):
    
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



