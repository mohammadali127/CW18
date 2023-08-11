from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter your password'}))