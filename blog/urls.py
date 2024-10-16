from django.urls import path

from .views import PostsListView, PostsTagListView, PostDetailView, PostsListSearchView, PutLikeView, PutDislikeView, PutWaterView, CommentChangeView


urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('search/', PostsListSearchView.as_view(), name='search_blog'),
    path('tags/<slug:tag_slug>/', PostsTagListView.as_view(), name='tag_list'),
    path('<slug:post_slug>/', PostDetailView.as_view(), name='post_detail'),

    path('put_like/<int:post_pk>/', PutLikeView.as_view(), name='put_like'),
    path('put_dislike/<int:post_pk>/', PutDislikeView.as_view(), name='put_dislike'),
    path('put_water/<int:post_pk>/', PutWaterView.as_view(), name='put_water'),

    path('comment_change/<int:comment_pk>/', CommentChangeView.as_view(), name='comment_change'),
]