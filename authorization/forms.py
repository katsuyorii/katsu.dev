from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    """ Форма авторизации пользователей """
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Введите email',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Введите пароль',
    }))

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(username=email, password=password)
        if user is None:
            raise forms.ValidationError('Неправильный email или пароль.')
        
        self.cleaned_data['user'] = user
        return self.cleaned_data