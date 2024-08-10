from django.views.generic import ListView, DetailView

from .models import Course


class CoursesListView(ListView):
    """ Представление для страницы сайта - «Курсы» """
    model = Course
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог курсов'

        return context


class CourseDetailView(DetailView):
    """ Представление для страницы отдельного выбранного курса """
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'
    slug_url_kwarg = 'course_slug'

    def get_queryset(self):
        queryset = Course.objects.filter(slug=self.kwargs['course_slug']).prefetch_related('themes__lessons')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title

        return context
