
from django.urls import path
from users.views import Profiles, create_book, user_login,register
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(),name='login'),
    path("register/",register,name='register'),
    path("profiles/", Profiles.as_view(), name="get_all_profiles"),
    path("books/", create_book.as_view(), name="create_book"),
]