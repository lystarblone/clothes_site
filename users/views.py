from django.urls import reverse, reverse_lazy
from .forms import LoginUserForm, ProfileUserForm, RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Authentication"}
    
    def get_success_url(self):
        return reverse_lazy("main_page")

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Registration"}

    def get_success_url(self):
        return reverse_lazy("users:login")
    
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {"title": "Profile"}


    def get_success_url(self):
        return reverse_lazy("users:profile")
    
    def get_object(self, queryset = None):
        return self.request.user
    
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("change_password_done")
    template_name = "users/change_pass.html"
    success_url = reverse_lazy("users:profile")

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'users/password_reset_email.txt'
    html_email_template_name = 'users/password_reset_email.html'

    def send_mail(self, subject_template_name, email_template_name, context, from_email, to_email, html_email_template_name=None):
        super().send_mail(
            subject_template_name=subject_template_name,
            email_template_name=email_template_name,
            context=context,
            from_email=from_email,
            to_email=to_email,
            html_email_template_name=html_email_template_name,
        )