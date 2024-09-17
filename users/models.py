from django.db import models
from django.contrib.auth.models import AbstractUser

from handlers.validators import ban_words_validator
from .validators import mime_type_validator


class User(AbstractUser):
    """ Кастомная модель пользователя, включающая в себя email и аватар """
    email = models.EmailField(verbose_name='Адрес эл. почты пользователя', unique=True)
    username = models.CharField(verbose_name='Никнейм', max_length=30, validators=[ban_words_validator])
    first_name = models.CharField(verbose_name='Имя пользователя', max_length=150, null=True, blank=True, validators=[ban_words_validator])
    last_name = models.CharField(verbose_name='Фамилия пользователя', max_length=150, null=True, blank=True, validators=[ban_words_validator])
    avatar = models.ImageField(verbose_name='Изображение профиля', upload_to='users_profile_avatars', null=True, blank=True, validators=[mime_type_validator])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email