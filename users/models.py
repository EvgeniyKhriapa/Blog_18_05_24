from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_birth = models.DateField(blank=True, null=True, verbose_name='День народження')
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name='Фото')

    class Meta:
        verbose_name_plural = 'Профіль користувачів'

    def __str__(self):
        return str(self.user)
