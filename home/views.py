from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def list_view(request):
    task_list = Todo.objects.all()
    return render(request, 'todolist.html', {'task': task_list})


def Add_todo(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        todo_dis = data.get('todo_dis')

        Todo.objects.create(
            title=title,
            todo_dis=todo_dis
        )

        return redirect('/')


def todo_completed(request, todo_id):
    task = Todo.objects.get(id=todo_id)
    task.completed = True
    task.save()
    return redirect('/')


def delete_todo(request, todo_id):
    queryset = Todo.objects.get(id=todo_id)
    queryset.delete()
    return redirect('/')
