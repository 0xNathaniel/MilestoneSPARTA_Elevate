from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from .models import Reminder

@shared_task
def send_reminders():
    now = timezone.now()
    reminders = Reminder.objects.filter(date__lte=now, completed=False)

    for reminder in reminders:
        # Send email
        send_mail(
            reminder.title,
            f"Hello {reminder.user.username},\n\nThis is a reminder for {reminder.title} on {reminder.date}.",
            'from@example.com',  # Replace with your email
            [reminder.user.email],
            fail_silently=False,
        )
        # Mark the reminder as sent
        reminder.completed = True
        reminder.save()