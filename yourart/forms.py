from django import forms
from .models import Yourart

class YourartForm(forms.ModelForm):
    class Meta:
        model = Yourart
        fields = ['user' ,'title', 'image']
        widgets = {'user': forms.HiddenInput}

# class CommentForm(forms.Form):
#     content = forms.CharField(max_length=280,
#     widget=forms.Textarea(attrs={'placeholder': 'Add a comment...'})
#     )
