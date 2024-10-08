from celery import shared_task

from PIL import Image

from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import User
from .services import get_mime_type


@shared_task
def process_avatar_task(user_id, avatar_path):
    """ Метод задачи в Celery для ресайза изображения и удаления EXIF-данных """
    user = User.objects.get(pk=user_id)
    mime_type = get_mime_type(user.avatar)
        
    avatar = Image.open(avatar_path)
    avatar = avatar.resize((130, 130))

    clean_avatar = Image.new(avatar.mode, avatar.size)
    clean_avatar.putdata(list(avatar.getdata()))

    buffer = BytesIO()
    clean_avatar.save(buffer, format='PNG')
    buffer.seek(0)

    new_avatar = InMemoryUploadedFile(
        buffer, None, f'{user.email}_avatar.png', mime_type, buffer.tell(), None
    )

    user.avatar.save(f'{user.email}_avatar.png', new_avatar)
    user.save()