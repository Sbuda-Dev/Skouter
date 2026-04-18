from rest_framework import serializers
from .models import ScoutProfile

class ScoutProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoutProfile
        fields = ['id', 'organization', 'verified']

        