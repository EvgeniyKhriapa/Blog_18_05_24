from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import LoginForm


def user_login(request):
    """Вхід користувачів"""
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main:topics')
                else:
                    return HttpResponse('Авторизацію не пройдено!')
            else:
                return redirect('users:register')
    return render(request, 'registration/login.html', {'form': form})


def logged(request):
    """Вихід користувача"""
    if request.method == 'POST':
        logout(request)
        return redirect('main:home')
    return render(request, 'registration/logged.html')


def register(request):
    """Реєстрація користувачів"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return render(request, 'registration/register_done.html', {'form': form})
    return render(request, 'registration/register.html', {'form': form})

