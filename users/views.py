from django.views.generic import TemplateView


class ProfileView(TemplateView):
    """ Представление для страницы профиля пользователя """
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['title'] = 'Профиль'

            return context
