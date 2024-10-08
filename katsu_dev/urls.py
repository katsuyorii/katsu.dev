"""
URL configuration for katsu_dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Library urls

    path("__debug__/", include("debug_toolbar.urls")),
    path('ckeditor5/', include('django_ckeditor_5.urls')),


    # Apps urls
    
    path('', include('core.urls')),
    path('courses/', include('courses.urls')),
    path('training/', include('training.urls')),
    path('blog/', include('blog.urls')),
    path('auth/', include('authorization.urls')),
    path('accounts/', include('users.urls')),
]


'''
    Отображение медиа файлов в режиме тестирования приложения (DEBUG = True)
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Объявление для кастомной страницы ошибки 404
handler404 = 'handlers.views.custom_404'
