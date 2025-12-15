
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        Task.objects.create(title=request.POST.get('title'))
    return redirect('task_list')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')
