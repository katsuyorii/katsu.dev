from django.contrib import admin

from .models import Course, Theme, Lesson, LessonMaterial, LessonQuestion


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Theme)
admin.site.register(LessonMaterial)
admin.site.register(LessonQuestion)
