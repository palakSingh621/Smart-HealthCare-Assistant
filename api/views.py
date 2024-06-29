from rest_framework import generics
from .models import HealthData
from .serializers import HealthdataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .services import get_health_recommendation

class healthdataViewSet(generics.ListAPIView):
    queryset = HealthData.objects.all()
    serializer_class = HealthdataSerializer

# @api_view(['POST'])
# def health_recommendation(request):
#     user_data = request.data
#     recommendation = get_health_recommendation(user_data)
#     return Response({'recommendation': recommendation})
# urlpatterns += [
#     path('recommendation/', health_recommendation),
# ]