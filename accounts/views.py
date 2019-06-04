from rest_framework import generics

from . import models
from . import serializers

class UserCreate(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer