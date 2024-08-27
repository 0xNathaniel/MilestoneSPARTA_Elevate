from django.contrib import admin
from .models import Tasks

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    
admin.site.register(Tasks, TasksAdmin)