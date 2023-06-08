from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import django
from django.contrib.auth.models import User
from django.forms import PasswordInput, TextInput, CharField


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = CharField(label='Повторить пароль', widget=PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={
        'class': 'form-control',
    }))
