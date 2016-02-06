from django.contrib.auth.models import User

from core.models import Places
from rest_framework import serializers



class PlacesSerializer(serializers.HyperlinkedModelSerializer):

    # Reads the user.owner attribute passed along from request
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Places
