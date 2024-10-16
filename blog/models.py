from django.db import models
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field

from users.models import User
from handlers.validators import ban_words_validator


class Tag(models.Model):
    """ Модель тегов для постов """
    name = models.CharField(verbose_name='Наименование', max_length=128, unique=True, db_index=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=128, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tag_list", kwargs={"tag_slug": self.slug})
    

class Post(models.Model):
    """ Модель поста """
    title = models.CharField(verbose_name='Наименование поста', max_length=128, unique=True, db_index=True)
    slug = models.SlugField(verbose_name='Слаг', max_length=128, unique=True, db_index=True)
    short_description = models.CharField(verbose_name='Краткое описание поста', max_length=255)
    body = CKEditor5Field(verbose_name='Содержимое поста', config_name='default')
    created_date = models.DateTimeField(verbose_name='Дата и время создания поста', auto_now_add=True)
    time_reading = models.PositiveSmallIntegerField(verbose_name='Время чтения')
    tags = models.ManyToManyField(verbose_name='Теги поста', to=Tag)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"post_slug": self.slug})
    
    def get_count_likes(self):
        """ Метод получения количества лайков у выбранного поста """
        return self.likes.count()
    
    def get_count_dislike(self):
        """ Метод получения количества дизлайков у выбранного поста """
        return self.dislikes.count()
    
    def get_count_water(self):
        """ Метод получения количества "воды" у выбранного поста """
        return self.waters.count()
    

class Like(models.Model):
    """ Модель лайка для постов """
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Пост', to=Post, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return f'{self.user.email} | {self.post.title}'
    

class Dislike(models.Model):
    """ Модель дизлайка для постов """
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Пост', to=Post, on_delete=models.CASCADE, related_name='dislikes')

    class Meta:
        verbose_name = 'Дизлайк'
        verbose_name_plural = 'Дизлайки'

    def __str__(self):
        return f'{self.user.email} | {self.post.title}'
    

class Water(models.Model):
    """ Модель "воды" для постов """
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Пост', to=Post, on_delete=models.CASCADE, related_name='waters')

    class Meta:
        verbose_name = 'Вода'
        verbose_name_plural = 'Вода'

    def __str__(self):
        return f'{self.user.email} | {self.post.title}'
    

class Comment(models.Model):
    """ Модель комментария к посту """
    user = models.ForeignKey(verbose_name='Пользователь', to=User, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Пост', to=Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(verbose_name='Дата и время создания комментария', auto_now_add=True)
    body = models.TextField(verbose_name='Текст комментария', validators=[ban_words_validator])

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.user.email} | {self.post.title} | {self.created_date} | {self.body}'
    
    def get_absolute_url(self):
        return reverse("comment_change", kwargs={"comment_pk": self.pk})