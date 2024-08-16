from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from .views import CoursesListView, CourseDetailView, LessonDetailView


urlpatterns = [
    path('', cache_page(60*15)(CoursesListView.as_view()), name='courses_list'),
    path('<slug:course_slug>/', cache_page(60*15)(CourseDetailView.as_view()), name='course_detail'),
    path('<slug:course_slug>/lessons/<slug:lesson_slug>', cache_page(60*15)(login_required(LessonDetailView.as_view())), name='lesson_detail'),
]