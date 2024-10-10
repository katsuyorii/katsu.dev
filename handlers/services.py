import json
import os

from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    """ Кастомная реализация хранения файлов у CKEditor5 """
    location = os.path.join(settings.MEDIA_ROOT, "ckeditor_upload_files")
    base_url = urljoin(settings.MEDIA_URL, "ckeditor_upload_files/")


def get_banned_words():
    """ Функция загрузки запретных слов """
    with open(settings.BASE_DIR  / 'banned_words.json', 'r') as file:
        banned_words_dict = json.load(file)

    banned_words = banned_words_dict.get('words')
    return banned_words
