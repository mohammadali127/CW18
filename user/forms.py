from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

