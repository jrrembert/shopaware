from django.shortcuts import render
from core.models import Places
from core.serializers import PlacesSerializer
from rest_framework import viewsets



# Create your views here.

class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
