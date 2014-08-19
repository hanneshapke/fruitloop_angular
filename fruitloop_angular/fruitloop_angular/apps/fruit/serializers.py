from rest_framework import serializers
from .models import FruitLocation


class FruitSerializer(serializers.ModelSerializer):
    fruit_name = serializers.RelatedField(source='fruit_type')

    class Meta:
        model = FruitLocation
        fields = ('id', 'address',
                  'comment',
                  'fruit_type', 'fruit_name',
                  'latitude', 'longitude',)
