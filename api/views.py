from rest_framework import generics
from .models import HealthData
from .serializers import HealthdataSerializer

class healthdataViewSet(generics.ListAPIView):
    queryset = HealthData.objects.all()
    serializer_class = HealthdataSerializer