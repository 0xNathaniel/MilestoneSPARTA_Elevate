from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Goal, Subgoal

# Create your views here.
def home(request):
    goals = Goal.objects.filter(user=request.user).order_by('-created_at')

    return render(request, "subgoal/home.html", {
        "goals": goals,
    })

def subgoal(request, goal_id):
    goals = Goal.objects.filter(user=request.user).order_by('-created_at')
    goal_choice = Goal.objects.get(id=goal_id)
    subgoals = Subgoal.objects.filter(user=request.user, goal=goal_choice).order_by('-created_at')
    
    return render(request, "subgoal/home.html", {
        "goals": goals,
        "subgoals": subgoals,
    })

def add_goal(request):
    if request.method == "POST":
        goal = request.POST["goal"]
        if goal:
            Goal.objects.create(
                user = request.user,
                title = goal
            )
        return HttpResponseRedirect(reverse("subgoal:home"))
    
def delete_goal(request, goal_id):
    pass
    
def add_subgoal(request):
    if request.method == "POST":
        goal_id_choice = request.POST["goal_id_choice"]
        goal_choice = Goal.objects.get(id=goal_id_choice)
        title = request.POST["title"]
        deadline = request.POST["deadline"]
        priority = request.POST["priority"]
        status = request.POST["status"]

        Subgoal.objects.create(
            user=request.user,
            title=title,
            deadline=deadline,
            priority=priority,
            status=status,
            goal=goal_choice
            )
        return HttpResponseRedirect(reverse("subgoal:home"))
    
    goals = Goal.objects.filter(user=request.user)
    return render(request, "subgoal/add_subgoal.html", {
        "goals": goals
    })
    
def delete_subgoal(request, subgoal_id):
    if request.method == "POST":
        subgoal = Subgoal.objects.get(user=request.user, id=subgoal_id)
        subgoal.delete()
        return HttpResponseRedirect(reverse("subgoal:home"))

def update_subgoal(request, subgoal_id):
    if request.method == "POST":
        subgoal = Subgoal.objects.get(user=request.user, id=subgoal_id)
        
        subgoal.deadline = request.POST["deadline"]
        subgoal.priortity = request.POST["priority"]
        subgoal.status = request.POST["status"]
        subgoal.save()
        
        return HttpResponseRedirect(reverse("subgoal:home"))

    return render(request, "subgoal/update_subgoal.html", {
        "subgoal_id": subgoal_id
    })