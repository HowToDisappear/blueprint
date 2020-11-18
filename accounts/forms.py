from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Account


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, max_length=30)

class RegisterForm(forms.ModelForm):
    password_confirmation = forms.CharField(widget=forms.PasswordInput, max_length=30)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput,
            'email': forms.EmailInput,
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmation = cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise ValidationError("Password confirmation didn't match password, please try again.")


class AccountFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
    
    def clean(self):
        cleaned_data = super().clean()
        for field in self.Meta.fields:
            if not cleaned_data.get(field):
                del cleaned_data[field]



class AccountFormAccount(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'id': 'image'})
        self.fields['crop_params'].widget.attrs.update({'id': 'crop_params'})

    av_action = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.HiddenInput(attrs={'id': 'av_action'})
        )
    class Meta:
        model = Account
        fields = ['image', 'crop_params']
