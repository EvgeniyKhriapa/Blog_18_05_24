from django.shortcuts import render


def home(request):
    """Головна сторінка"""
    return render(request, 'main/home.html')
