from django.forms import ModelForm
from django import forms

from .models import Feedback


class FeedbackForm(ModelForm):
    """ Форма для отправки сообщения обратной связи """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'main-login-auth-block-input',
        'placeholder': 'Введите ваше имя',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'main-login-auth-block-input',
        'placeholder': 'Введите ваш email',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'main-login-auth-block-input',
        'placeholder': 'Введите здесь ваше сообщение...',
        'rows': '4',
    }))

    class Meta:
        model = Feedback
        fields = ('username', 'email', 'message')