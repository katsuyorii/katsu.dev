from django.views.generic import ListView

from .models import QuestionTraining, Grade, Category


class TrainingListView(ListView):
    """ Представление для страницы - «Тренажер» """
    model = QuestionTraining
    template_name = 'training/training_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        queryset = QuestionTraining.objects.all().select_related('grade').prefetch_related('categories')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тренажер'
        context['categories'] = Category.objects.all()
        context['grades'] = Grade.objects.all()

        return context