import magic


def get_mime_type(avatar_file):
    """ Метод для получения mime типа загружаемого изображения """
    mime = magic.Magic(mime=True)
    mime_type = mime.from_buffer(avatar_file.file.read(1024))

    avatar_file.file.seek(0)
    
    return mime_type