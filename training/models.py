from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class Grade(models.Model):
    """ Модель уровня вопроса по градации опыта и скилла (Traine, Junior, Middle, Senior) """
    name = models.CharField(verbose_name='Наименование', max_length=128, unique=True, db_index=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=128, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Уровень скилла и опыта'
        verbose_name_plural = 'Уровни скилла и опыта'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("grade_list", kwargs={"grade_slug": self.slug})


class Category(models.Model):
    """ Модель категории вопроса (Python, Web, основы и т.д.) """
    name = models.CharField(verbose_name='Наименование', max_length=128, unique=True, db_index=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=128, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category_list", kwargs={"category_slug": self.slug})
    

class QuestionTraining(models.Model):
    """ Модель вопроса в тренажере """
    title = models.CharField(verbose_name='Наименование вопроса', max_length=128, unique=True, db_index=True)
    answer = CKEditor5Field(verbose_name='Ответ на вопрос', config_name='default')
    grade = models.ForeignKey(verbose_name='Уровень скилла и опыта', to=Grade, on_delete=models.CASCADE)
    categories = models.ManyToManyField(verbose_name='Категории', to=Category)

    class Meta:
        verbose_name = 'Вопрос тренажера'
        verbose_name_plural = 'Вопросы тренажера'

    def __str__(self):
        return self.title

