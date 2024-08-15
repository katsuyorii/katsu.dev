from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View
from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.tokens import default_token_generator 
from django.utils.http import urlsafe_base64_decode 

from .forms import LoginForm, RegistrationForm, ForgotPasswordForm, ForgotPasswordChangeForm
from .tasks import activate_email_task, forgot_password_task


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
        messages.success(self.request, 'Вы успешно вошли в систему!')

        return super().form_valid(form)
        
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка заполнения формы!')
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

        messages.success(self.request, 'Регистрация прошла успешно!')
        
        return super().form_valid(form)
            
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка заполнения формы!')
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
    

class ActivateEmailRepeatSendView(View):
    """ Представление для повторной отправки сообщения на email пользователя для подтверждения """
    def get(self, request): 
        activate_email_task.delay(request.user.pk)
        return HttpResponseRedirect(reverse_lazy('activate_email_done'))
    

class ForgotPasswordView(FormView):
    """ Представления для страницы восстановления пароля ввода email пользователя """
    form_class = ForgotPasswordForm
    template_name = 'authorization/forgot_password.html'

    def get_success_url(self):
        return reverse_lazy('forgot_password_done')

    def form_valid(self, form): 
        email_form = form.cleaned_data['email']
        user = user_model.objects.get(email=email_form) 
        forgot_password_task.delay(user.pk)

        return super().form_valid(form)
            
    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Восстановление пароля'

            return context


class ForgotPasswordDoneView(TemplateView):
    """ Представление для страницы ожидания подтверждения восстановления пароля пользователя """
    template_name = 'authorization/forgot_password_done.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Восстановление пароля'

            return context


class ForgotPasswordCheckView(View):
    """ Представление для проверки отправленной ссылки на подтверждения на email пользователя """
    def get(self, request, uidb64, token):  
        try:  
            uid = urlsafe_base64_decode(uidb64)  
            user = user_model.objects.get(pk=uid)  
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):  
            user = None
        if user is not None and default_token_generator.check_token(user, token):  
            return HttpResponseRedirect(reverse_lazy('forgot_password_change',  kwargs={'uidb64': uidb64}))
        else:  
            return HttpResponseRedirect(reverse_lazy('forgot_password'))


class ForgotPasswordChangeView(FormView):
    """ Представление для страницы ввода нового пароля после восстановления пароля """
    form_class = ForgotPasswordChangeForm
    template_name = 'authorization/forgot_password_change.html'

    def get(self, request, uidb64):
        return super().get(self, request, uidb64)

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form): 
        uid = urlsafe_base64_decode(self.kwargs['uidb64'])  
        user = user_model.objects.get(pk=uid)

        new_password = form.cleaned_data['password2']

        user.set_password(new_password)
        user.save()

        messages.success(self.request, 'Вы успешно сменили пароль!')

        return super().form_valid(form)
            
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка заполнения формы!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Восстановление пароля'

            return context