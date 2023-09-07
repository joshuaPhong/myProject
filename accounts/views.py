from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CustomUserCreationForm
from accounts.forms import CustomUserChangePasswordForm


class ChangePasswordView(CreateView):
    form_class = CustomUserChangePasswordForm
    success_url = reverse_lazy('done')
    template_name = 'registration/password_change_form.html'


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
