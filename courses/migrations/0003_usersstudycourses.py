# Generated by Django 5.0.7 on 2024-10-14 10:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_lesson_materials_alter_lesson_questions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersStudyCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(to='courses.course', verbose_name='Курсы')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Изучаемые курсы пользователей',
                'verbose_name_plural': 'Изучаемые курсы пользователей',
            },
        ),
    ]
