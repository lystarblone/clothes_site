from django import forms
from .models import User, Type

class AuthForm(forms.Form):
    pass
'''
    log = forms.CharField(max_length=100)
    password = forms.CharField(max_length=150)
    fun_text = forms.CharField(widget=forms.Textarea(), required=False)
    categories = forms.ModelChoiceField(queryset=Type.objects.all
    email = forms.EmailField(max_length=100)
    password = forms.PasswordInput()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone = forms.N'''