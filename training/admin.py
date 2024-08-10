from django.contrib import admin

from .models import Grade, Category, QuestionTraining


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(QuestionTraining)
class QuestionTrainingAdmin(admin.ModelAdmin):
    list_display = ['title', 'answer', 'grade']