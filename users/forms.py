from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm


class CustomPasswordChangeForm(forms.Form):
    """Зміна пароля користувача"""
    current_password = forms.CharField(widget=forms.PasswordInput, label='Поточний пароль')
    new_password = forms.CharField(widget=forms.PasswordInput, label='Новий пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Підтвердити новий пароль')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if not self.user.check_password(current_password):
            self.add_error('current_password', 'Поточний пароль невірний')

        if new_password != confirm_password:
            self.add_error('confirm_password', 'Новий пароль і підтвердження не співпадають')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label='І"мя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UsersRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторити пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        """Валідація паролю"""
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Паролі не співпадають!')
        return cd['password2']


class UsersEditForm(forms.ModelForm):
    """Редагування даних користувача"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


class ProfileEditForm(forms.ModelForm):
    """Редагування профілю користувача"""
    class Meta:
        model = Profile
        fields = ['date_birth', 'photo']


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Введіть вашу електронну адресу")
