from django.views.generic import ListView

from .models import Post, Tag


class PostsListView(ListView):
    """ Представление для страницы сайта - «Блог» """
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_date').prefetch_related('tags')

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