from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    username = models.CharField(blank=True, max_length=255, unique=True)
    email = models.EmailField(blank=True, max_length=255)
    password = models.CharField(blank=True, max_length=255)
