import json

from django.conf import settings


def get_banned_words():
    """ Функция загрузки запретных слов """
    with open(settings.BASE_DIR  / 'banned_words.json', 'r') as file:
        banned_words_dict = json.load(file)

    banned_words = banned_words_dict.get('words')
    return banned_words
