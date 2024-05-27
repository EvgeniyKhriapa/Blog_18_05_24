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


class Image(models.Model):
    """Завантаження картинок за темою"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Коментар до фото')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, verbose_name='Фото')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')

    class Meta:
        verbose_name_plural = 'Фото по темам'

    def __str__(self):
        return self.title


class Audio(models.Model):
    """Завантаження аудіо за темою"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Коментар до аудіо')
    audio = models.FileField(upload_to='audios/%Y/%m/%d/', blank=True, verbose_name='Аудіо')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання аудіо')

    class Meta:
        verbose_name_plural = 'Аудіо'

    def __str__(self):
        return self.title


class Video(models.Model):
    """Завантаження відео за темою"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Коментар до відео')
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, verbose_name='Відео')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання відео')

    class Meta:
        verbose_name_plural = 'Відео'

    def __str__(self):
        return self.title


class File(models.Model):
    """Завантаження файлів за темою"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Коментар до файлу')
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True, verbose_name='Файл')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання файлу')

    class Meta:
        verbose_name_plural = 'Файли'

    def __str__(self):
        return self.title
