from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def home(request):
    """Головна сторінка"""
    return render(request, 'main/home.html')


def topics(request):
    """Показ всіх теми"""
    topics = Topic.objects.order_by('-date')
    return render(request, 'main/topics.html', {'topics': topics})


def topic(request, topic_id):
    """Показ однієї теми"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date')
    return render(request, 'main/topic_one.html', {'topic': topic, 'entries': entries})


def new_topic(request):
    """Запис нової теми"""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/topics.html', {'form': form})
    else:
        form = TopicForm()
    return render(request, 'main/new_topic.html', {'form': form})


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


def edit_entry(request, entry_id):
    """Редагування запису до теми"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method == 'POST':
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/topics.html', {'form': form, 'entry': entry, 'topic': topic})
    else:
        form = EntryForm(instance=entry)
    return render(request, 'main/edit_entry.html', {'form': form, 'entry': entry})
