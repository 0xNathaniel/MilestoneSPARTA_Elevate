from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.home, name="home"),
    path("add-task/", views.add_task, name="add"),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete")
]