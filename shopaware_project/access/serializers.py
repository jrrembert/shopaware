from django.contrib.auth.models import User

from core.models import Places
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    places = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Places.objects.all())

    class Meta:
        model = User
