from django.contrib import admin

from .models import Post, Tag, Like, Dislike, Water, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_date', 'time_reading', 'short_description', 'body']
    prepopulated_fields = {'slug': ['title']}
    date_hierarchy = 'created_date'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']


@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']


@admin.register(Water)
class WaterAdmin(admin.ModelAdmin):
    list_display = ['user', 'post']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_date', 'body']
    date_hierarchy = 'created_date'