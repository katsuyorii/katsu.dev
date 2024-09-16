import magic


def get_mime_type(avatar_path):
    """ Метод для получения mime типа загружаемого изображения """
    with open(avatar_path, 'rb') as file:
        mime = magic.Magic(mime=True)
        mime_type = mime.from_buffer(file.read(1024))
    
    return mime_type