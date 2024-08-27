from django.urls import path
from . import views

app_name = "subgoal"

urlpatterns = [
    path("", views.home, name="home"),
    path("/goal/<int:goal_id>", views.subgoal, name="goal"),
    path("add_goal", views.add_goal, name="add_goal"),
    path("delete_goal/<int:goal_id>", views.delete_goal, name="delete_goal"),
    path("/add_subgoal", views.add_subgoal, name="add_subgoal"),
    path("delete_subgoal/<int:subgoal_id>", views.delete_subgoal, name="delete_subgoal"),
    path("/update_subgoal/<int:subgoal_id>", views.update_subgoal, name="update_subgoal"),
]