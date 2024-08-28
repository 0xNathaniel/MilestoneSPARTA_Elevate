from django.urls import path
from . import views

app_name = "reminder"

urlpatterns = [
    path("", views.home, name="home"),
    path("add_reminder/", views.add_reminder, name="add_reminder"),
    path("delete_reminder/<int:reminder_id>/", views.delete_reminder, name="delete_reminder"),
    path("update_reminder/<int:reminder_id>/", views.update_reminder, name="update_reminder"),
]