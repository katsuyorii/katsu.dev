from django.contrib.auth import get_user_model

from celery import shared_task

from .services import SendEmail


user_model = get_user_model()

@shared_task
def activate_email_task(user_pk):
    """ Таск для celery по активации аккаунта пользователя """
    user = user_model.objects.get(pk=user_pk)
    send_email = SendEmail(user=user)  
    send_email.send_activate_email() 
