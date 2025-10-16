from pyexpat.errors import messages
from tokenize import Comment
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
# from users import serializers
from users.models import admin_user,book,profile,Author
from users.forms import UserForm
import json 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from users.serializers import ProfileSerializer, BookSerializer, AuthorSerializer


def home(request):
    return HttpResponse("Welcome to the Book Store")

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data.decode("utf-8"))
        print(type(data))
        print(f"{data}")
        print(f"{data['phone_number']}")
        phone_number = data["phone_number"]
        password = data["password"]
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            #messages.success(request, "Login successful")
            return redirect("home")
        else:
            #messages.error(request, "Invalid login")
            return redirect("register")

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = request.body
        data = json.loads(data.decode("utf-8"))
        form = UserForm(data=data)
        if form.is_valid():

            phone_number = data["phone_number"]
            password = data["password"]

            User = admin_user.objects.create(phone_number=phone_number)
            User.set_password(password)
            profile.objects.create(user=User,address=data.get("address"),national_code=data.get("national_code"))
            User.save()
            
            return HttpResponse (f"user {User.phone_number} created successfully")
        else:
            return HttpResponse("Invalid form data", status=400)

# def get_all_profile(request):
#     if request.method == "GET":
#         profiles_list = []
#         profiles = list(profile.objects.all())

#         for user_profile in profiles:
#             profiles_list.append({"user": user_profile.user.phone_number,"national_code": user_profile.national_code,"address": user_profile.address})
#         return JsonResponse(profiles_list,safe=False )


def get_all_profile(request):
    if request.method == "GET":
        profiles = profile.objects.all()
        return render(request, "profiles.html", {"profiles": profiles})

class Profiles(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = profile.objects.all()
    serializer_class = ProfileSerializer
# class create_book(generics.CreateAPIView):


#     permission_classes = [IsAuthenticated]
#     queryset = book.objects.all()
#     serializer_class = book_serializer
#     def create(self, serializer):
#         serializer.save()

class create_book (generics.CreateAPIView):
    serializer_class = BookSerializer
    model = book


class author_registration (generics.CreateAPIView):
    serializer_class = AuthorSerializer
    model = Author

class author_list (generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class book_list (generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = book.objects.all()
