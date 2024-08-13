from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login

from .forms import LoginForm


class LoginView(FormView):
    """ Представление для страницы авторизации пользователей """
    form_class = LoginForm
    template_name = 'authorization/login.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form): 
        user = form.cleaned_data['user']
        
        login(self.request, user)

        return super().form_valid(form)
        
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'

        return context
