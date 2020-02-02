from django import forms
from .models import AuthUser


class RegistrationForm(forms.ModelForm):
    email = forms.CharField(max_length=254, required=True)

    class Meta:
        model = AuthUser
        fields = ('email', 'password', 'username')
