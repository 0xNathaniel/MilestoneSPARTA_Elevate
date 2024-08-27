from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Tasks

# Create your views here.
def home(request):
    tasks = Tasks.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, "todo/home.html", {
        "tasks": tasks
    })

def add_task(request):
    if request.method == "POST":
        task = request.POST["task"]
        if task:
            Tasks.objects.create(user=request.user, title=task.capitalize())
    return HttpResponseRedirect(reverse("todo:home"))

def delete_task(request, task_id):
    if request.method == "POST":
        task = Tasks.objects.get(user=request.user, id=task_id)
        task.delete()
        return HttpResponseRedirect(reverse("todo:home"))