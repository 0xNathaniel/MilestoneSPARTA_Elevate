from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "users/index.html")

def register_view(request):
    return render(request, "users/register.html")

def login_view(request):
    return render(request, "users/login.html")

def logout_view(request):
    return render(request, "users/logout.html")