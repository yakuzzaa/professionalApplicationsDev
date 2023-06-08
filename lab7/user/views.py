from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm


# Create your views here.

class SignUP(CreateView):
    form_class = RegisterUserForm
    template_name = 'user/signup.html'
    success_url = "/"


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/signup.html'
    success_url = "/"

    def get_success_url(self):
        return "/"
