from django import forms
from .models import User

class AuthForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]