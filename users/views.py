from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView, UpdateView, CreateView
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import logout, get_user_model
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import PasswordChangeForm, InfoProfileChangeForm, ReviewForm
from .tasks import process_avatar_task
from authorization.tasks import activate_email_task
from courses.models import UsersStudyCourses, Review, Course


user_model = get_user_model()


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
        messages.success(request, 'Вы успешно вышли из аккаунта!')
        return redirect(reverse_lazy('index'))
    

class PasswordChangeView(PasswordChangeView):
    """ Представление для страницы смены пароля пользователя """
    form_class = PasswordChangeForm
    template_name = 'users/profile_password_change.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Вы успешно сменили пароль!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка заполнения формы!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Смена пароля'

        return context


class InfoProfileChangeView(UpdateView):
    """ Представление для редактирования профиля пользователя """
    model = user_model
    form_class = InfoProfileChangeForm
    template_name = 'users/profile_info_change.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        current_user = user_model.objects.get(pk=self.request.user.pk)
        new_email = form.cleaned_data['email']
        new_avatar = form.cleaned_data['avatar']

        messages.success(self.request, 'Изменения прошли успешно!')

        if current_user.email == new_email:
            self.object = form.save(commit=False)
            self.object.save()
            
            if not current_user.avatar == new_avatar:
                process_avatar_task.delay(self.request.user.pk, self.request.user.avatar.path)

            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            self.object = form.save(commit=False)
            self.object.is_active = False
            self.object.save()
            activate_email_task.delay(self.request.user.pk)
            return HttpResponseRedirect(reverse_lazy('activate_email_done'))
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка заполнения формы!')
        return super().form_invalid(form)

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'

        return context


class MyCoursesListView(TemplateView):
    """ Представление для страницы сайта - «Мои курсы» """
    template_name = 'users/my_courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои курсы'
        context['my_courses'] = UsersStudyCourses.objects.filter(user=self.request.user).prefetch_related('course')

        return context


class ReviewAddView(CreateView):
    """ Представление для страницы добавления отзыва на курс """
    model = Review
    form_class = ReviewForm
    template_name = 'users/review.html'

    def get_success_url(self):
        return reverse_lazy('my_courses')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        selected_course = Course.objects.get(slug=self.kwargs['course_slug'])

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.course = selected_course
            review.save()

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, 'Отзыв успешно был отправлен!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Ошибка заполнения формы!')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оставить отзыв на курс'

        return context