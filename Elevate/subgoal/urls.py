from django.urls import path
from . import views

app_name = "subgoal"

urlpatterns = [
    path("", views.home, name="home"),
]