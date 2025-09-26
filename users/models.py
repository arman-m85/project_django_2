from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from users.user_manager import CustomUserManager
# Create your models here.

class admin_user(AbstractUser):
    phone_number = models.CharField(max_length = 11,unique = True)

    USERNAME_FIELD = "phone_number"

    objects = CustomUserManager()


class customer(admin_user):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)



    


