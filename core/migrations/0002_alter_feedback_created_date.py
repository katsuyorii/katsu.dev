# Generated by Django 5.0.7 on 2024-08-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время отправки сообщения'),
        ),
    ]
