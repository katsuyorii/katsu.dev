from functools import wraps

from django.http import Http404

from .models import Comment


def creator_comment_only(func):
    """ Декоратор для проверки является ли данный пользователь создателем комментария, чтобы дать доступ к его редактированию/удалению """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            comment_pk = kwargs['comment_pk']
            user_comm = Comment.objects.get(pk=comment_pk, user=request.user)
        except:
            raise Http404()
        
        return func(request, *args, **kwargs)
    
    return wrapper