from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CoursesListView, CourseDetailView, LessonDetailView


urlpatterns = [
    path('', CoursesListView.as_view(), name='courses_list'),
    path('<slug:course_slug>/', CourseDetailView.as_view(), name='course_detail'),
    path('<slug:course_slug>/lessons/<slug:lesson_slug>', login_required(LessonDetailView.as_view()), name='lesson_detail'),
]