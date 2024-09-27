# Generated by Django 5.0.7 on 2024-09-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(db_index=True, max_length=128, verbose_name='Наименование урока'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='name',
            field=models.CharField(db_index=True, max_length=128, verbose_name='Наименование раздела курса'),
        ),
    ]
