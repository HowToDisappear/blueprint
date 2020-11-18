from django import forms

class TestForm(forms.Form):
    your_random_text = forms.CharField(max_length=10)

class SigninForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=30)