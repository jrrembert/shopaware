from core.models import Places
from rest_framework import serializers



class PlacesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Places
