from rest_framework import serializers

from .models import Coordinate

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ['id', 'x', 'y', 'z']