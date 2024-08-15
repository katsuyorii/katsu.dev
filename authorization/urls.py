from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import LoginView, RegistrationView, ActivateEmailDoneView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('activate_email_done/', login_required(ActivateEmailDoneView.as_view()), name='activate_email_done')
]