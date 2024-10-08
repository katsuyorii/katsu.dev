from django.contrib.auth.tokens import default_token_generator  
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.urls import reverse_lazy  
from django.utils.http import urlsafe_base64_encode 

from users.models import User


user_model = get_user_model()


class SendEmail:
    """ Класс отправки сообщения на email пользователя """
    def __init__(self, user : User):
        self.user = user
        self.current_site = Site.objects.get_current().domain
        self.token = default_token_generator.make_token(self.user)
        self.uid = urlsafe_base64_encode(str(self.user.pk).encode())

    def send_activate_email(self):
        activate_url = reverse_lazy(  
            "activate_email_check", kwargs={"uidb64": self.uid, "token": self.token}  
        ) 
        subject = f"Активация аккаунта на сайте - {self.current_site}"  
        message = (  
            f"Благодарим за регистрацию на сайте {self.current_site}.\n"  
            "Для активации учётной записи, пожалуйста перейдите по ссылке:\n"  
            f"https://{self.current_site}{activate_url}\n"  
        )  

        self.user.email_user(subject=subject, message=message)

    def send_forgot_password(self):
        forgot_psw_url = reverse_lazy(  
            "forgot_password_check", kwargs={"uidb64": self.uid, "token": self.token}  
        )  
        subject = f"Восстановление пароля"  
        message = (  
            f"Привет, {self.user.username}!\n"  
            "Вы получили это письмо, потому что мы приняли запрос на восстановление пароля для вашей учетной записи. Для восстановления пароля пройдите по ссылке:\n"  
            f"https://{self.current_site}{forgot_psw_url}\n"  
        )  

        self.user.email_user(subject=subject, message=message)
