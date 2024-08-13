from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model

from handlers.validators import ban_words_validator


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


class InfoProfileChangeForm(forms.ModelForm):
    """ Форма для редактирования информации о профиле пользователя """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите никнейм',
        'class': 'main-login-auth-block-input', 
    }), validators=[ban_words_validator])

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Введите адрес эл. почты',
        'class': 'main-login-auth-block-input', 
    }))
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя',
        'class': 'main-login-auth-block-input', 
    }), required=False, validators=[ban_words_validator])

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите фамилию пользователя',
        'class': 'main-login-auth-block-input', 
    }), required=False, validators=[ban_words_validator])

    avatar = forms.ImageField(required=False, widget=forms.FileInput())
    
    class Meta:
        user_model = get_user_model()
        model = user_model
        fields = ['username', 'email', 'avatar', 'first_name', 'last_name']