from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import SignUpUserForm

# Create your views here.
def home(request):
    # If user is not authenticated, redirect to login page
    if not request.user.is_authenticated:
        return render(request, "user/home1.html")
    # If user is authenticated, render home page
    else:
        return render(request, "user/home2.html")
    
def sign_up(request):
    # If request method is POST, validate form
    if request.method == "POST":
        form = SignUpUserForm(request.POST)
        # If form is valid, authenticate user
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse("user:home"))
    # If user has not signed up, send user creation form
    else:
        form = SignUpUserForm()
    # If request method is not POST, render sign_up page
    return render(request, "user/sign_up.html", {
        "form": form
    })

def login_view(request):
    # If request method is POST, authenticate user
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # If user is authenticated, login user
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("user:home"))
        else:
            return render(request, "user/login.html", {
                "message": "Invalid Username/Password"
            })
    # If request method is not POST, render login page
    return render(request, "user/login.html")
        
def logout_view(request):
    logout(request)
    return render(request, "user/login.html")