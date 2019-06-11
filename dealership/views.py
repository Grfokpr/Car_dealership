from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from . import models
from . import serializers

class DealershipList(generics.ListCreateAPIView):
    queryset = models.Dealership.objects.all()
    serializer_class = serializers.DealershipSerializer



    # all cars return
    # all cars for dealership return