from django.shortcuts import render

from django.shortcuts import render, redirect , get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'to_do/index.html', {'tasks': tasks, 'form': form})

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('/')



def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'to_do/edit.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all().order_by('due_date')
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def toggle_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

