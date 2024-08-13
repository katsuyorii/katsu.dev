from django.views.generic import View, TemplateView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.shortcuts import redirect


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