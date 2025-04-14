from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    class Meta:
        model = get_user_model()
        fields = ["email", "password"]

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Account name", widget=forms.TextInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput())

    class Meta():
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        labels = {
            "first_name": "First name",
            "last_name": "Last name",
            "email": "Email",
        }
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('The email you entered is already exist.')
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')
        return username