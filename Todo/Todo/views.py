from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks": tasks, "title": "Todo"})


def add(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "add.html", {"form": form})
    return render(request, "add.html", {"form": TaskForm(), "title": "Add Task"})


def update(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except ObjectDoesNotExist:
        print("LOG: Data doens't Exist ")
    else:
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("index")
            else:
                return render(request, "update.html", {"form": form})
        else:
            # print(TaskForm(instance=task))
            return render(
                request,
                "update.html",
                {"form": TaskForm(instance=task), "title": "update Task"},
            )
    return redirect("index")


def delete(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        print("LOG: Data doens't Exist")
    else:
        task.delete()
    return redirect("index")


def remove(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except ObjectDoesNotExist:
        print("LOG: Data doens't Exist ")
    else:
        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True
        task.save()
    return redirect("index")
