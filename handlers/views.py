from django.shortcuts import render


def custom_404(request,  exception):
    """ Функция для кастомной страницы ошибки 404"""
    return render(request, 'page404.html', status=404)