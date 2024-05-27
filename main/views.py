from django.shortcuts import render, redirect
from .models import Topic, Entry, Image, Audio, Video, File
from .forms import TopicForm, EntryForm, ImageForm, FileForm, VideoForm, AudioForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def home(request):
    """Головна сторінка"""
    return render(request, 'main/home.html')


@login_required
def topics(request):
    """Показ всіх теми"""
    topics = Topic.objects.filter(owner=request.user).order_by('-date')
    return render(request, 'main/topics.html', {'topics': topics})


@login_required
def topic(request, topic_id):
    """Показ однієї теми та всіх записів до неї"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date')
    new_photos = topic.image_set.order_by('-date_added')
    new_audios = topic.audio_set.order_by('-date_added')
    new_videos = topic.video_set.order_by('-date_added')
    new_files = topic.file_set.order_by('-date_added')
    return render(request, 'main/topic_one.html', {'topic': topic, 'entries': entries, 'new_photos': new_photos, 'new_audios': new_audios, 'new_videos': new_videos, 'new_files': new_files})


@login_required
def new_topic(request):
    """Запис нової теми"""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.owner = request.user
            form.save()
            return render(request, 'main/topics.html', {'form': form})
    else:
        form = TopicForm()
    return render(request, 'main/new_topic.html', {'form': form})


@login_required
def new_entry(request, topic_id):
    """Новий запис до теми"""
    topic = Topic.objects.get(id=topic_id)
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return render(request, 'main/topics.html', {'form': form, 'topic': topic})
    else:
        form = EntryForm()
    return render(request, 'main/new_entry.html', {'form': form, 'topic': topic})


@login_required
def edit_entry(request, entry_id):
    """Редагування запису до теми"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method == 'POST':
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/topics.html', {'form': form, 'entry': entry, 'topic': topic})
    else:
        form = EntryForm(instance=entry)
    return render(request, 'main/edit_entry.html', {'form': form, 'entry': entry})


@login_required
def del_topic(request, topic_id):
    """Видалення теми"""
    top = Topic.objects.get(id=topic_id)
    if request.method == 'GET':
        top.delete()
        return redirect('main:topics')
    else:
        return render('main/home.html', {'top': top})


@login_required
def new_photo(request, topic_id):
    """Завантаження картинку за темою"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = ImageForm()
    else:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.topic = topic
            new_photo.save()
            form.save()
            return redirect('main:topic', topic_id=topic_id)
    return render(request, 'main/photo.html', {'topic': topic, 'form': form})


@login_required
def new_audio(request, topic_id):
    """Завантаження аудіо за темою"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = AudioForm()
    else:
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            new_audio = form.save(commit=False)
            new_audio.topic = topic
            new_audio.save()
            form.save()
            return redirect('main:topic', topic_id=topic_id)
    return render(request, 'main/new_audio.html', {'topic': topic, 'form': form})


@login_required
def new_video(request, topic_id):
    """Завантаження відео за темою"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = VideoForm()
    else:
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.topic = topic
            new_video.save()
            form.save()
            return redirect('main:topic', topic_id=topic_id)
    return render(request, 'main/new_video.html', {'topic': topic, 'form': form})


@login_required
def new_file(request, topic_id):
    """Завантаження файлу за темою"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = FileForm()
    else:
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = form.save(commit=False)
            new_file.topic = topic
            new_file.save()
            form.save()
            return redirect('main:topic', topic_id=topic_id)
    return render(request, 'main/new_file.html', {'topic': topic, 'form': form})
