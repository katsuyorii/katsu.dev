from django.db import models
from django.core.validators import FileExtensionValidator


class SliderImage(models.Model):
    """ Модель изображения слайдера для главной страницы """
    image = models.ImageField(verbose_name='Изображение', upload_to='slider_images', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'svg', 'webp', 'heif', 'avif'])])
    alt_text = models.CharField(verbose_name='Альтернативный текст для изображения', max_length=255)

    class Meta:
        verbose_name = 'Изображение слайдера'
        verbose_name_plural = 'Изображения слайдера'

    def __str__(self):
        return self.alt_text


class Feedback(models.Model):
    """ Модель обратной связи с пользователями """
    username = models.CharField(verbose_name='Имя пользователя', max_length=255)
    email = models.EmailField(verbose_name='Адрес эл. почты пользователя')
    message = models.TextField(verbose_name='Сообщение пользователя')
    created_date = models.DateTimeField(verbose_name='Дата и время отправки сообщения', auto_created=True)

    class Meta:
        verbose_name = 'Сообщение обратной связи'
        verbose_name_plural = 'Сообщения обратной связи'

    def __str__(self):
        return f'{self.email} | {self.created_date} | {self.message}'
