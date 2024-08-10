from django.urls import path

from .views import PostsListView, PostsTagListView, PostDetailView


urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('tags/<slug:tag_slug>/', PostsTagListView.as_view(), name='tag_list'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),
]