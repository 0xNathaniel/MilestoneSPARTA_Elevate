from django.contrib import admin
from .models import Goal, Subgoal

# Register your models here.
class GoalAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    
class SubgoalAdmin(admin.ModelAdmin):
    list_display = ("goal", "title", "deadline", "status", "priority", "created_at")
    
admin.site.register(Goal, GoalAdmin)
admin.site.register(Subgoal, SubgoalAdmin)