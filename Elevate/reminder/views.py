from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Reminder

# Create your views here.
def home(request):
    reminders = Reminder.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "reminder/home.html", {
        "reminders": reminders
    })

def add_reminder(request):
    if request.method == "POST":
        title = request.POST["title"]
        date = request.POST["date"]

        Reminder.objects.create(
            user=request.user,
            title=title,
            date=date,
            completed=False
            )
        return HttpResponseRedirect(reverse("reminder:home"))

    return render(request, "reminder/add_reminder.html")
    
def delete_reminder(request, reminders_id):
    if request.method == "POST":
        Reminder = Reminder.objects.get(user=request.user, id=reminders_id)
        Reminder.delete()
        return HttpResponseRedirect(reverse("reminder:home"))
    
def update_reminder(request, reminders_id):
    if request.method == "POST":
        reminder = Reminder.objects.get(user=request.user, id=reminders_id)
        
        reminder.date = request.POST["date"]
        reminder.description = request.POST["description"]
        reminder.completed = request.POST["completed"]
        reminder.save()

        return HttpResponseRedirect(reverse("reminder:home"))

    return render(request, "reminder/update_reminder.html", {
        "reminders_id": reminders_id
    })