from django import forms
from django.contrib.auth.models import User
from .models import Profile


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
