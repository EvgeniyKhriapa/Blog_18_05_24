from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import password_reset_request

app_name = 'users'
urlpatterns = [
    # Сторінка входу користувача
    path('user_login/', views.user_login, name='user_login'),
    # Сторінка виходу користувача
    path('logged/', views.logged, name='logged'),
    # Сторінка реєстрації користувача
    path('register/', views.register, name='register'),
    # Сторінка зміни даних профілю користувача
    path('profile_edit_user/', views.profile_edit_user, name='profile_edit_user'),
    # Сторінка зміни пароля
    path('password_change_user/', views.password_change_user, name='change_password_user'),
    # Скидання пароля через електронну пошту
    path('password-reset/', password_reset_request, name='password_reset_request'),
    # Відправлення запиту на зміну пароля
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    # Підтвердження про відправлення листа електронною поштою
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
]
