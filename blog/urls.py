from django.urls import path

from .views import PostsListView, PostsTagListView


urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('tags/<slug:tag_slug>/', PostsTagListView.as_view(), name='tag_list'),
]