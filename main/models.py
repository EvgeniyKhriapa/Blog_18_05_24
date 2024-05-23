from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Модель теми"""
    text = models.CharField(max_length=200, verbose_name='Тема')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Теми'

    def __str__(self):
        """Повернення запису назви теми"""
        return self.text


class Entry(models.Model):
    """Модель записів для теми"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Записи до тем'

    def __str__(self):
        """Повернення запису теми"""
        return f"{self.text[:100]}..."
