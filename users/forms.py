from django import forms
from django.contrib.auth.forms import PasswordChangeForm


class PasswordChangeForm(PasswordChangeForm):
    """ Форма для смены пароля пользователя """
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите текущий пароль',
        'class': 'main-login-auth-block-input',
    }))

    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите новый пароль',
        'class': 'main-login-auth-block-input',
    }))

    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите новый пароль',
        'class': 'main-login-auth-block-input',
    }))