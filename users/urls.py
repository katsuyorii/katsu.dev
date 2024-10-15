from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ProfileView, LogoutView, PasswordChangeView, InfoProfileChangeView, MyCoursesListView, ReviewAddView


urlpatterns = [
    path('profile/', login_required(ProfileView.as_view()), name='profile'),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('my_courses/', login_required(MyCoursesListView.as_view()), name='my_courses'),
    path('review/<slug:course_slug>/', login_required(ReviewAddView.as_view()), name='review'),
    path('password_change/', login_required(PasswordChangeView.as_view()), name='password_change'),
    path('info_profile_change/', login_required(InfoProfileChangeView.as_view()), name='info_profile_change'),
]