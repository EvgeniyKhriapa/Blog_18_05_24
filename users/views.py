from django.shortcuts import render


def login_out(request):
    """Вихід користувача"""
    return render(request, 'registration/login_out.html')
