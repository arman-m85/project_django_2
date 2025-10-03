
from django.urls import path
from users.views import user_login,register,get_all_profile
urlpatterns = [
    path('login/', user_login,name='login'),
    path("register/",register,name='register'),
    path("profiles/", get_all_profile, name="get_all_profiles"),
]