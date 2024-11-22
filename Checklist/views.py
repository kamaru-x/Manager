from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Checklist.models import Title, Task
from datetime import datetime
today = datetime.today()

# Create your views here.

@login_required
def checklist(request):
    titles = Title.objects.all()

    for title in titles:
        if not Task.objects.filter(title=title, date=today).exists():
            Task.objects.create(title=title, date=today)

    tasks = Task.objects.filter(date=today).order_by('title__title')

    dates = Task.objects.values('date').distinct().order_by('-date')

    context = {
        'page' : 'checklist',
        'tasks' : tasks,
        'dates' : dates
    }
    return render(request, 'checklist/checklist.html', context)

@login_required
def mark_task_completed(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id)
        task.is_completed = True
        task.save()
    return redirect('checklist')


@login_required
def tasks(request, date):
    date = datetime.strptime(date, '%Y-%m-%d').date()

    tasks = Task.objects.filter(date=date).order_by('title__title')

    context = {
        'page' : 'checklist',
        'tasks' : tasks,
    }

    return render(request, 'checklist/tasks.html', context)