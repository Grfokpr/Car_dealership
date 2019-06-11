from django.contrib.auth.models import AbstractUser
from django.db import models
from dealership.models import Dealership
class CustomUser(AbstractUser):

    username = models.CharField(blank=True, max_length=255, unique=True)
    email = models.EmailField(blank=True, max_length=255)
    password = models.CharField(blank=True, max_length=255)
    user_type = models.IntegerField(blank=True,default=0)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE,blank=True,null=True)