from django import forms
from .models import AuthUser


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = AuthUser
        fields = ('username', 'email', 'password')
