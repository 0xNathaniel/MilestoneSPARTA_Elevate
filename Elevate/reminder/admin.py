from django.contrib import admin
from .models import Reminder

# Register your models here.
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "completed", "created_at")
    
admin.site.register(Reminder, ReminderAdmin)