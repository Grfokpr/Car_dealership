from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8,required=True)

    def create(self, state):
        user = User.objects.create_user(state['username'],state['email'],state['password'])
        return user

    class Meta():
        model = User
        fields = ('id','username','email', 'password')


# Create your models here.
