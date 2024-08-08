from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .models import SliderImage, Feedback
from .forms import FeedbackForm
from courses.models import Course, Review


class IndexView(TemplateView):
    """ Представление для главной страницы сайта """
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Платформа онлайн обучения katsu.dev'
        context['slider_images'] = SliderImage.objects.all()
        context['courses'] = Course.objects.all().order_by('amount_students')[:3]
        context['reviews'] = Review.objects.all().order_by('-created_date')[:3].select_related('user', 'course')

        return context
    

class AboutView(TemplateView):
    """ Представление для страницы сайта - «О проекте» """
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О проекте'

        return context


class ContactsView(CreateView):
    """ Представление для страницы сайта - «Контакты» """
    model = Feedback
    form_class = FeedbackForm
    template_name = 'core/contacts.html'

    def get_success_url(self):
        return reverse_lazy('contacts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'

        return context