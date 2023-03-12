from django.db import models
from django.core.validators import FileExtensionValidator

from src.base.services import get_path_upload_avatar, validate_size_image


# Create your models here.
class AuthUser(models.Model):
    '''
    Модель пользователя на платформе
    '''
    email = models.EmailField(max_length=150, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)

    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg']), validate_size_image]
    )

    @property
    def is_authenticated(self):
        '''
        Всегда возвращает True. Это способ узнать был ли пользователь аунтефицирован
        :return:
        '''
        return True

    def __str__(self):
        return self.email


class Followers(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='owner', )
    subscriber = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='sibscribers', )

    def __str__(self):
        return f'{self.subscriber} podpisan na {self.user}'


class SocialLink(models.Model):
    '''
    Модель ссылок на соц сети пользователя
    '''
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links', )
    link = models.URLField(max_length=100)

    def __str__(self):
        return self.user