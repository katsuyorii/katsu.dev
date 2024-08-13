from django.views.generic import View, TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import PasswordChangeForm


class ProfileView(TemplateView):
    """ Представление для страницы профиля пользователя """
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Профиль'

            return context


class LogoutView(View):
    """ Представление для функции выхода из аккаунта """
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse_lazy('index'))
    

class PasswordChangeView(PasswordChangeView):
    """ Представление для страницы смены пароля пользователя """
    form_class = PasswordChangeForm
    template_name = 'users/profile_password_change.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Смена пароля'

        return context