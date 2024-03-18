from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks": tasks})


def add(request):
    if request.method == "POST":
        print(request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "add.html", {"form": form})
    return render(request, "add.html", {"form": TaskForm(), "title": "Add Task"})


def edit(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task:
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("index")
            else:
                return render(request, "edit.html", {"form": form})
        else:
            print(TaskForm(instance=task))
            return render(
                request,
                "edit.html",
                {"form": TaskForm(instance=task), "title": "Edit Task", "task": task},
            )
    return redirect("index")


def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task:
        task.delete()
    return redirect("index")


def remove(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task:
        task.is_done = True
        task.save()

    return redirect("index")
