from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import UserSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.models import User

class UserCreate(APIView):

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        queryset = User.objects.all()
        serializer_class = UserSerializer(queryset,many=True)

        return Response(serializer_class.data)