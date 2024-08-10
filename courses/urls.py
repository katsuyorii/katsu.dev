from django.urls import path

from .views import CoursesListView, CourseDetailView


urlpatterns = [
    path('', CoursesListView.as_view(), name='courses_list'),
    path('<slug:course_slug>/', CourseDetailView.as_view(), name='course_detail'),
]