from django.forms import ValidationError

from .services import get_banned_words


def ban_words_validator(value):
    """ Валидатор проверки введенного текста на наличие запретных слов """
    banned_words = get_banned_words()
    
    for word in banned_words:
        if word in value.lower():
            raise ValidationError('В вашем тексте есть неприемлемые слово или слова. Пожалуйста, исправьте их.')