from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "subgoal_progresstracker/index.html")