from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # Домашня сторінка
    path('', views.home, name='home'),
    # Список тем
    path('topics/', views.topics, name='topics'),
    # Окрема тема
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Нова тема
    path('new_topic/', views.new_topic, name='new_topic'),
    # Новий запис до теми
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # Зміна запису до теми
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    # Видалення теми
    path('delete_topic/<int:topic_id>/', views.del_topic, name='del_topic'),
    # Завантаження фото за темою
    path('new_photo/<int:topic_id>/', views.new_photo, name='new_photo'),
    # Завантаження аудіо за темою
    path('new_audio/<int:topic_id>/', views.new_audio, name='new_audio'),
    # Завантаження відео за темою
    path('new_video/<int:topic_id>/', views.new_video, name='new_video'),
    # Завантаження файлу за темою
    path('new_file/<int:topic_id>/', views.new_file, name='new_file'),
]
