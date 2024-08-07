from django.views.generic import TemplateView

from .models import SliderImage


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Платформа онлайн обучения katsu.dev'
        context['slider_images'] = SliderImage.objects.all()

        return context