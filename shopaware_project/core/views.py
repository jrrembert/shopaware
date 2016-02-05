from django.http import Http404, HttpResponse
from django.shortcuts import render

from core.models import Places
from core.serializers import PlacesSerializer

from rest_framework import viewsets, status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer


class PlacesView(generics.ListCreateAPIView):
    """
    Get a list of places.

    HTTP Methods: GET, POST
    """
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class PlacesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides GET (single instance), PUT, and DELETE methods for Places.
    """
    queryset = Places.objects.all()
    serializer_class = PlacesSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
