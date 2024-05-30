from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import LoginForm, UsersRegistrationForm, UsersEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import PasswordResetRequestForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail


def password_reset_request(request):
    """Скидання пароля через електронну пошту"""
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                for user in associated_users:
                    subject = "Запит на скидання паролю"
                    email_template_name = "password_reset_email.txt"
                    context = {
                        "email": user.email,
                        'domain': request.META['HTTP_HOST'],
                        'site_name': 'Ваш сайт',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email_content = render_to_string(email_template_name, context)
                    try:
                        send_mail(subject, email_content, 'admin@yourdomain.com', [user.email], fail_silently=False)
                    except Exception as e:
                        messages.error(request, 'Виникла помилка при надсиланні електронного листа: ' + str(e))
                    messages.success(request, 'Лист для скидання паролю успішно надісланий.')
            else:
                messages.error(request, 'Користувач з такою електронною адресою не знайдений.')
            return render(request, 'registration/password_reset_request.html')
    else:
        form = PasswordResetRequestForm()
    return render(request, "registration/password_reset_request.html", {"form": form})


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
        form = UsersRegistrationForm()
    else:
        form = UsersRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            login(request, new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile_edit_user(request):
    """Редагування даних користувача"""
    if request.method != 'POST':
        user_form = UsersEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    else:
        user_form = UsersEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    return render(request, 'user/profile_edit_user.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def password_change_user(request):
    """Зміна пароля користувача"""
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            return redirect('main:topics')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'registration/password_change_user.html', {'form': form})
