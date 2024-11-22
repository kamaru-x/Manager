from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Todo.models import Todo
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def todo(request):
    todos = Todo.objects.all()
    high = todos.filter(priority='High').count()
    normal = todos.filter(priority='Normal').count()
    low = todos.filter(priority='Low').count()

    context = {
        'page' : 'todo',
        'todos' : todos,
        'high' : high,
        'normal' : normal,
        'low' : low,
    }
    return render(request, 'todo/todo.html', context)

@login_required
def add_todo(request):
    if request.method == 'POST':
        priority = request.POST.get('priority')
        title = request.POST.get('title')

        try:
            Todo.objects.create(priority=priority, title=title)
            messages.success(request, 'Todo added')
            return redirect('todo')

        except Exception as exception:
            messages.warning(request,str(exception))
            return redirect('add-todo')

    context = {
        'page' : 'todo',
    }
    return render(request,'todo/todo-add.html',context)

@login_required
def mark_todo_completed(request, id):
    if request.method == "POST":
        todo = Todo.objects.get(id=id)
        todo.is_completed = True
        todo.save()
    return redirect('todo')