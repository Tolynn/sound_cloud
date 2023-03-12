from django.core.validators import ValidationError
def get_path_upload_avatar(instance, file):
    '''
    Построение пути к файлу /media/avatar/user_id/photo.jpg
    :return:
    '''
    return f'avatar/{instance.id}/{file}'

def validate_size_image(file_obj):
    '''
    Проверка размера файла
    :param file_obj:
    :return:
    '''
    megabyte_limit=2
    if file_obj.size>megabyte_limit*1024*1024:
        raise ValidationError(f"MAX size {megabyte_limit}MB")
