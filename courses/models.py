import os

from django.db import models
from django.core.validators import FileExtensionValidator
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field

from users.models import User
from handlers.validators import ban_words_validator


class LessonQuestion(models.Model):
    """ Модель вопросов к уроку """
    name = models.CharField(verbose_name='Наименование вопроса', max_length=128)
    answer = models.TextField(verbose_name='Ответ на вопрос')

    class Meta:
        verbose_name = 'Вопрос к уроку'
        verbose_name_plural = 'Вопросы к уроку'

    def __str__(self):
        return self.name


class LessonMaterial(models.Model):
    """ Модель материалов к уроку (файлы) """
    class Extension(models.TextChoices):
        ZIP = "ZIP", '.zip'
        JPG = "JPG", '.jpg'
        PDF = "PDF", '.pdf'

    file = models.FileField(verbose_name='Файл', upload_to='lesson_materials/', validators=[FileExtensionValidator(['zip', 'jpg', 'pdf'])])
    extension = models.CharField(verbose_name='Тип файла', max_length=3, choices=Extension.choices)

    class Meta:
        verbose_name = 'Материал к уроку'
        verbose_name_plural = 'Материалы к уроку'

    def __str__(self):
        return self.file.name
    
    def only_filename(self):
        """ Метод возвращающий только наименование файла и его расширение, без полного пути к папке media """
        return os.path.basename(self.file.name)


class Lesson(models.Model):
    """ Модель урока раздела курса """
    name = models.CharField(verbose_name='Наименование урока', max_length=128)
    slug = models.SlugField(verbose_name='Слаг', max_length=255, unique=True, db_index=True)
    body = CKEditor5Field(verbose_name='Содержимое урока', config_name='default')
    materials = models.ManyToManyField(verbose_name='Материалы к уроку', to=LessonMaterial, blank=True)
    questions = models.ManyToManyField(verbose_name='Вопросы к уроку', to=LessonQuestion, blank=True)
    created_date = models.DateTimeField(verbose_name='Дата и время добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['created_date']

    def __str__(self):
        return self.name


class Theme(models.Model):
    """ Модель раздела курса """
    name = models.CharField(verbose_name='Наименование раздела курса', max_length=128, unique=True, db_index=True)
    description = models.CharField(verbose_name='Описание раздела', max_length=255)
    lessons = models.ManyToManyField(verbose_name='Уроки', to=Lesson)
    created_date = models.DateTimeField(verbose_name='Дата и время добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Раздел курса'
        verbose_name_plural = 'Разделы курса'
        ordering = ['created_date']

    def __str__(self):
        return self.name


class Course(models.Model):
    """ Модель курса """
    class Status(models.TextChoices):
        HIT = "HIT", 'Хит'
        UPDATE = "UPD", 'Обновлено'
        NEW = "NEW", 'Новинка'

    title = models.CharField(verbose_name='Наименование курса', max_length=128, unique=True, db_index=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=255, unique=True, db_index=True)
    short_description = models.CharField(verbose_name='Краткое описание курса', max_length=255)
    full_description = models.TextField(verbose_name='Полное описание курса')
    amount_students = models.PositiveIntegerField(verbose_name='Количество учащихся на курсе', default=0)
    amount_hours = models.PositiveSmallIntegerField(verbose_name='Количество часов курса')
    poster = models.ImageField(verbose_name='Постер курса', upload_to='course_posters/')
    price = models.PositiveIntegerField(verbose_name='Цена курса', null=True, blank=True)
    discount = models.PositiveSmallIntegerField(verbose_name='Скидка на курс (%)', null=True, blank=True)
    status = models.CharField(verbose_name='Статус курса', max_length=3, choices=Status.choices, default=Status.NEW, null=True, blank=True)
    themes = models.ManyToManyField(verbose_name='Разделы курса', to=Theme)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"course_slug": self.slug})
    


class Review(models.Model):
    """ Модель отзыва на курс """
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(verbose_name='Курс', to=Course, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='Текст отзыва', validators=[ban_words_validator])
    created_date = created_date = models.DateTimeField(verbose_name='Дата и время создания отзыва', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.user.email} | {self.course.title} | {self.created_date}'
