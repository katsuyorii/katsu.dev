from django.forms import ModelForm
from django import forms

from .models import Comment


class CommentForm(ModelForm):
    """ Форма для отправки комментария """
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'post-flex-comments-input',
        'placeholder': 'Напишите здесь свой комментарий...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ['body']