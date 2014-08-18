from rest_framework import serializers
from .models import FruitLocation


class FruitSerializer(serializers.ModelSerializer):

    class Meta:
        model = FruitLocation
        fields = ('id', 'address',
                  'comment', 'fruit_type',
                  'latitude', 'longitude',)
