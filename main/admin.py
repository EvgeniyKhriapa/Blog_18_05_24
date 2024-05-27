from django.contrib import admin
from .models import Topic, Entry, Image, File, Video, Audio

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Image)
admin.site.register(File)
admin.site.register(Video)
admin.site.register(Audio)
