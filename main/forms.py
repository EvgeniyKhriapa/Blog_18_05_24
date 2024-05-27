from django import forms
from .models import Topic, Entry, Image, Audio, Video, File


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']


class ImageForm(forms.ModelForm):
    """Форма для завантаження картинок"""
    class Meta:
        model = Image
        fields = ('title', 'image')


class AudioForm(forms.ModelForm):
    """Форма для завантаження аудіо"""
    class Meta:
        model = Audio
        fields = ['title', 'audio']


class VideoForm(forms.ModelForm):
    """Форма для завантаження відео"""
    class Meta:
        model = Video
        fields = ['title', 'video']


class FileForm(forms.ModelForm):
    """Форма для завантаження файлів"""
    class Meta:
        model = File
        fields = ['title', 'file']
