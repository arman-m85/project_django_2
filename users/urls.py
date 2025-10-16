
from django.urls import path
from users.views import Profiles, author_list, user_login, register, create_book, author_registration, book_list
#from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(),name='login'),
    path("register/",register,name='register'),
    path("profiles/", Profiles.as_view(), name="get_all_profiles"),
    path("books/", create_book.as_view(), name="create_book"),
    path("authors/", author_registration.as_view(), name="create_author"),
    path("authorsList/", author_list.as_view(), name="get_all_authors"),
    path("booksList/", book_list.as_view(), name="get_all_books"),
]