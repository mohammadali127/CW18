from django import forms
from .models import User
from django.core.exceptions import ValidationError

class CreateUser(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        cd = super().clean
        p1 = cd.get('password1')
        p2 = cd.get('password1')
        if p1 != p2:
            raise ValidationError('passwords must match.')
