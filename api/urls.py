from django.urls import path
from .views import healthdataViewSet

urlpatterns = [
    path('healthdata/', healthdataViewSet.as_view()),
]