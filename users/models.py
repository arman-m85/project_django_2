from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from users.user_manager import CustomUserManager

# Create your models here.

class admin_user(AbstractUser):
    phone_number = models.CharField(max_length = 11,unique = True)
    username = models.CharField(max_length=150, null=True , blank= True,unique=False)
    USERNAME_FIELD = "phone_number"
    
    objects = CustomUserManager()


class customer(admin_user):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)



class profile(models.Model):
    user = models.ForeignKey(admin_user, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10,null=True, blank=True)
    address = models.CharField(max_length=300,null=True, blank=True)

 
    


 