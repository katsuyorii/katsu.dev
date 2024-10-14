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


class TrainingGradeListView(ListView):
    """ Представление для страницы фильтрации по скиллу и опыту """
    model = QuestionTraining
    template_name = 'training/training_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        queryset = QuestionTraining.objects.filter(grade__slug=self.kwargs['grade_slug']).select_related('grade').prefetch_related('categories')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Вопросы по опыту - «{self.kwargs['grade_slug']}»'
        context['categories'] = Category.objects.all()
        context['grades'] = Grade.objects.all()

        return context
    

class TrainingCategoriesListView(ListView):
    """ Представление для страницы фильтрации по категории """
    model = QuestionTraining
    template_name = 'training/training_list.html'
    context_object_name = 'questions'

    def get_queryset(self):
        queryset = QuestionTraining.objects.filter(categories__slug=self.kwargs['category_slug']).select_related('grade').prefetch_related('categories')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Вопросы по категории - «{self.kwargs['category_slug']}»'
        context['categories'] = Category.objects.all()
        context['grades'] = Grade.objects.all()

        return context
    

class TrainingListSearchView(ListView):
    """ Представление для поиска вопросов по названию """
    model = QuestionTraining
    template_name = 'training/training_list_search.html'
    context_object_name = 'questions'

    def get_queryset(self):
        filter_value = self.request.GET.get('filter')

        if filter_value == "":
            queryset = QuestionTraining.objects.none()
        else:
            queryset = QuestionTraining.objects.filter(title__icontains=filter_value).select_related('grade').prefetch_related('categories')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тренажер'
        context['categories'] = Category.objects.all()
        context['grades'] = Grade.objects.all()

        filter_value = self.request.GET.get('filter')
        context['filter_value'] = filter_value

        return context