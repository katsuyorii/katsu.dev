from django.urls import path

from .views import TrainingListView, TrainingGradeListView, TrainingCategoriesListView


urlpatterns = [
    path('', TrainingListView.as_view(), name='training_list'),
    path('grade/<slug:grade_slug>/', TrainingGradeListView.as_view(), name='grade_list'),
    path('categories/<slug:category_slug>/', TrainingCategoriesListView.as_view(), name='category_list'),
]