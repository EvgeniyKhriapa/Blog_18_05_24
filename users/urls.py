from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('logged/', views.logged, name='logged'),
    path('register/', views.register, name='register'),
    path('profile_edit_user/', views.profile_edit_user, name='profile_edit_user'),
]
