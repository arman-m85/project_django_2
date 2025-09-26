from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

def home(request):
    return HttpResponse("Welcome to the Book Store")


def user_login(request):
    if request.method == "POST":

        phone_number = request.POST["phone_number"]
        password = request.POST["password"]
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, "Login successful")
            return redirect("home")
        else:
            messages.error(request, "Invalid login")
            return redirect("register")

def register(request):
    return HttpResponse ("you should login first")
# Create your views here.
