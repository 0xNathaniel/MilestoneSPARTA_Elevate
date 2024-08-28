from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Reminder
from django.core.mail import send_mail
from django.utils import timezone

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
    
def update_reminder(request, reminder_id):
    if request.method == "POST":
        reminder = Reminder.objects.get(user=request.user, id=reminder_id)
        
        reminder.date = request.POST["date"]
        reminder.completed = request.POST["completed"]
        reminder.save()

        return HttpResponseRedirect(reverse("reminder:home"))

    return render(request, "reminder/update_reminder.html", {
        "reminder_id": reminder_id
    })
    
def delete_reminder(request, reminder_id):
    if request.method == "POST":
        reminder = Reminder.objects.get(user=request.user, id=reminder_id)
        reminder.delete()
        return HttpResponseRedirect(reverse("reminder:home"))