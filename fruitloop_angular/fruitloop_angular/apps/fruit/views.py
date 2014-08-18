from .models import FruitLocation
from .serializers import FruitSerializer
from rest_framework import generics


class FruitAPIList(generics.ListCreateAPIView):
    queryset = FruitLocation.objects.filter(
        latitude__isnull=False).filter(
        longitude__isnull=False)
    serializer_class = FruitSerializer


class FruitAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FruitLocation.objects.all()
    serializer_class = FruitSerializer
