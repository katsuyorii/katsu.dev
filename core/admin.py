from django.contrib import admin

from .models import SliderImage, Feedback


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'alt_text']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'message', 'created_date']
    date_hierarchy = 'created_date'
