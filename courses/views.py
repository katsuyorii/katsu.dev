from django.views.generic import ListView

from .models import Course


class CoursesListView(ListView):
    """ Представление для страницы сайта - «Курсы» """
    model = Course
    template_name = 'courses/courses.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог курсов'

        return context
