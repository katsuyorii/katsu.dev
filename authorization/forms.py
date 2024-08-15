from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password

from handlers.validators import ban_words_validator


user_model = get_user_model()


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
    

class RegistrationForm(forms.Form):
    """ Форма регистрации новых пользователей """
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Введите email',
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Введите никнейм',
    }), validators=[ban_words_validator])

    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Введите пароль',
    }), validators=[validate_password])
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Повторите пароль',
    }), validators=[validate_password])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Введенные пароли отличаются!')
        
        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if user_model.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже существует!')
        
        return email
    

class ForgotPasswordForm(forms.Form):
    """ Форма восстановления пароля ввода email """
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Введите ваш email',
    }))

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not user_model.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email не найден!')
        
        return email
    

class ForgotPasswordChangeForm(forms.Form):
    """ Форма ввода нового пароля после восстановления пароля """
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Введите новый пароль',
    }), validators=[validate_password])
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {
        'class': 'main-login-auth-block-input', 
        'placeholder': 'Повторите новый пароль',
    }), validators=[validate_password])
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Введенные пароли отличаются!')
        
        return password2
