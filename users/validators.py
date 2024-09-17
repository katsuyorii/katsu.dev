from django.forms import ValidationError

from .services import get_mime_type


def mime_type_validator(value):
    """ Валидатор проверки mime типа загружаемого файла """
    LIST_MIME_TYPES = ('image/jpeg', 'image/jpg', 'image/avif', 'image/png', 'image/svg+xml', 'image/webp', 'image/heic')
    current_mime_type = get_mime_type(value)

    if not current_mime_type in LIST_MIME_TYPES:
        raise ValidationError('Недопустимый формат файла. Допустимые форматы - .jpeg, .jpg, .png, .avif, .svg, .webp, .heic')