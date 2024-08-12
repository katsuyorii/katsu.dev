from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404
from django.db.models import Count

from .models import Post, Tag, Comment, Like


class PostsListView(ListView):
    """ Представление для страницы сайта - «Блог» """
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all().annotate(like_count=Count('likes')).order_by('-created_date').prefetch_related('tags')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог'
        context['tags'] = Tag.objects.all()

        return context
    

class PostsTagListView(ListView):
    """ Представление для страницы фильтрации по тегам """
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(tags__slug=self.kwargs['tag_slug']).order_by('-created_date').prefetch_related('tags')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Посты по тегу - «{self.kwargs['tag_slug']}»'
        context['tags'] = Tag.objects.all()

        return context
    

class PostDetailView(DetailView):
    """ Представлени для страницы отдельного поста """
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_queryset(self):
        queryset = Post.objects.filter(slug=self.kwargs['post_slug']).prefetch_related('tags')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        context['comments'] = Comment.objects.filter(post__slug=self.kwargs['post_slug']).order_by('-created_date').select_related('user')

        return context
    

class PutLikeView(View):
    """ Представления для кнопки - «Лайк» (огонек) """
    def get(self, request, *args, **kwargs):
        selected_post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        is_exists = Like.objects.filter(post=selected_post, user=request.user).exists()

        if not is_exists:
            like = Like(post=selected_post, user=request.user)
            like.save()
            color_text = 'red'
            count_likes = selected_post.get_count_likes()
        else:
            like = Like.objects.filter(post=selected_post, user=request.user)
            like.delete()
            color_text = '#767676'
            count_likes = selected_post.get_count_likes()

        return JsonResponse({'color_text': color_text, 'count_likes': count_likes})