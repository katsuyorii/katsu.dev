from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View
from django.contrib.auth import login, get_user_model
from django.contrib.auth.tokens import default_token_generator 
from django.utils.http import urlsafe_base64_decode 

from .forms import LoginForm, RegistrationForm
from .tasks import activate_email_task


user_model = get_user_model()


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
    """ Представление для страницы ожидания подтверждения активации аккаунта пользователя """
    template_name = 'authorization/activate_email_done.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Подтверждение E-mail'

            return context


class ActivateEmailCheckView(View):
    """ Представление для проверки отправленной ссылки на подтверждения на email пользователя """ 
    def get(self, request, uidb64, token):  
        try:  
            uid = urlsafe_base64_decode(uidb64)  
            user = user_model.objects.get(pk=uid)  
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):  
            user = None  
        if user is not None and default_token_generator.check_token(user, token):  
            user.is_active = True
            user.save()  
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('activate_email_confirm'))
        else:  
            return HttpResponseRedirect(reverse_lazy('activate_email_not_confirm'))


class ActivateEmailConfirmView(TemplateView):
    """ Представление для страницы успешного подтверждения email """
    template_name = 'authorization/activate_email_confirm.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Подтверждение E-mail'

            return context
    

class ActivateEmailErrorView(TemplateView):
    """ Представление для страницы ошибки подтверждения email """
    template_name = 'authorization/activate_email_not_confirm.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Подтверждение E-mail'

            return context