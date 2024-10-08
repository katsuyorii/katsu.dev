# Generated by Django 5.0.7 on 2024-10-06 19:42

import django.core.validators
import django.db.models.deletion
import django_ckeditor_5.fields
import handlers.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128, unique=True, verbose_name='Наименование курса')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('short_description', models.CharField(max_length=255, verbose_name='Краткое описание курса')),
                ('full_description', models.TextField(verbose_name='Полное описание курса')),
                ('amount_students', models.PositiveIntegerField(default=0, verbose_name='Количество учащихся на курсе')),
                ('amount_hours', models.PositiveSmallIntegerField(verbose_name='Количество часов курса')),
                ('poster', models.ImageField(upload_to='course_posters/', verbose_name='Постер курса')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена курса')),
                ('discount', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Скидка на курс (%)')),
                ('status', models.CharField(blank=True, choices=[('HIT', 'Хит'), ('UPD', 'Обновлено'), ('NEW', 'Новинка')], default='NEW', max_length=3, null=True, verbose_name='Статус курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='LessonMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='lesson_materials/', validators=[django.core.validators.FileExtensionValidator(['zip', 'jpg', 'pdf'])], verbose_name='Файл')),
                ('extension', models.CharField(choices=[('ZIP', '.zip'), ('JPG', '.jpg'), ('PDF', '.pdf')], max_length=3, verbose_name='Тип файла')),
            ],
            options={
                'verbose_name': 'Материал к уроку',
                'verbose_name_plural': 'Материалы к уроку',
            },
        ),
        migrations.CreateModel(
            name='LessonQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование вопроса')),
                ('answer', models.TextField(verbose_name='Ответ на вопрос')),
            ],
            options={
                'verbose_name': 'Вопрос к уроку',
                'verbose_name_plural': 'Вопросы к уроку',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование урока')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг')),
                ('body', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Содержимое урока')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('materials', models.ManyToManyField(to='courses.lessonmaterial', verbose_name='Материалы к уроку')),
                ('questions', models.ManyToManyField(to='courses.lessonquestion', verbose_name='Вопросы к уроку')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
                'ordering': ['created_date'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(validators=[handlers.validators.ban_words_validator], verbose_name='Текст отзыва')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания отзыва')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=128, unique=True, verbose_name='Наименование раздела курса')),
                ('description', models.CharField(max_length=255, verbose_name='Описание раздела')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время добавления')),
                ('lessons', models.ManyToManyField(to='courses.lesson', verbose_name='Уроки')),
            ],
            options={
                'verbose_name': 'Раздел курса',
                'verbose_name_plural': 'Разделы курса',
                'ordering': ['created_date'],
            },
        ),
        migrations.AddField(
            model_name='course',
            name='themes',
            field=models.ManyToManyField(to='courses.theme', verbose_name='Разделы курса'),
        ),
    ]
