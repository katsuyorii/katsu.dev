from django.contrib import admin

from .models import Course, Theme, Lesson, LessonMaterial, LessonQuestion, UsersStudyCourses, Review


""" Переопределение пустого поля на кастомное """
admin.AdminSite.empty_value_display = "---пусто---"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount_students', 'amount_hours', 'price', 'discount', 'status']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(LessonMaterial)
class LessonMaterialAdmin(admin.ModelAdmin):
    list_display = ['file', 'extension']


@admin.register(LessonQuestion)
class LessonQuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'answer']


@admin.register(UsersStudyCourses)
class UsersStudyCoursesAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'created_date', 'body']
    date_hierarchy = 'created_date'

