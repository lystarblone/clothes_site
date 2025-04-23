from django.urls import reverse_lazy
from django import forms
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, login
from .forms import (
    LoginUserForm,
    ProfileUserForm,
    RegisterUserForm,
    UserPasswordChangeForm
)
from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.shortcuts import redirect

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}

    def get_success_url(self):
        return reverse_lazy("main_page")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}

    def get_success_url(self):
        return reverse_lazy("users:login")


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {"title": "Профиль"}

    def get_success_url(self):
        return reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:profile")
    template_name = "users/change_pass.html"


class PasswordResetForm(BasePasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email не зарегистрирован.")
        return email


class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.txt'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')


def oauth_callback(request):
    provider_id = request.GET.get('provider_id')
    email = request.GET.get('email')

    User = get_user_model()
    user, created = User.objects.get_or_create(
        provider_id=provider_id,
        defaults={'email': email or f"{provider_id}@example.com"}
    )

    login(request, user)
    return redirect(reverse_lazy("main_page"))