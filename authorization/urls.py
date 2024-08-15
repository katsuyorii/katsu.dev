from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import LoginView, RegistrationView, ActivateEmailDoneView, ActivateEmailCheckView, ActivateEmailConfirmView, ActivateEmailErrorView, ActivateEmailRepeatSendView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('activate_email_done/', login_required(ActivateEmailDoneView.as_view()), name='activate_email_done'),
    path('activate_email_check/<uidb64>/<token>/', login_required(ActivateEmailCheckView.as_view()), name='activate_email_check'),
    path('activate_email_confirm/', login_required(ActivateEmailConfirmView.as_view()), name='activate_email_confirm'),
    path('activate_email_not_confirm/', login_required(ActivateEmailErrorView.as_view()), name='activate_email_not_confirm'),
    path('activate_email_repeat/', login_required(ActivateEmailRepeatSendView.as_view()), name='activate_email_repeat'),
]