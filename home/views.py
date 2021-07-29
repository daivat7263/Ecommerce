from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import CreateUserForm



def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method =="POST":
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request,"Account was created for " + user)
                return redirect("login")

        context = {"form": form}
        return render(request,"register.html",context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username= username, password=password)

            if user is not None:
                login(request,user)
                return redirect ("home")
            else:
                messages.info(request,"Username Or Password is Incorrect.!")

        context = {}
        return render(request,"login.html",context)

@login_required(login_url="login")
def index(request):
    return render(request,"index.html")





def logoutUser(request):
    logout(request)
    return redirect("login")

 