from rest_framework import serializers
from . import models

class DealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dealership
        fields = ('name', 'id', )