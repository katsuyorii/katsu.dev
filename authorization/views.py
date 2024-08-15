from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login, get_user_model

from .forms import LoginForm, RegistrationForm
from .tasks import activate_email_task


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
    

class RegistrationView(FormView):
    """ Представление для страницы регистрации новых пользователей """
    form_class = RegistrationForm
    template_name = 'authorization/registration.html'

    def get_success_url(self):
        return reverse_lazy('activate_email_done')

    def form_valid(self, form): 
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']

        user_model = get_user_model()

        user = user_model.objects.create_user(username=username, email=email, password=password1, is_active=False)
        login(self.request, user)
        activate_email_task.delay(user.pk)
        
        return super().form_valid(form)
            
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Регистрация'

            return context


class ActivateEmailDoneView(TemplateView):
    """ Страница ожидания подтверждения активации аккаунта пользователя """
    template_name = 'authorization/activate_email_done.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Подтверждение E-mail'

            return context