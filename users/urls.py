from django.urls import path

from .views import ProfileView, LogoutView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]