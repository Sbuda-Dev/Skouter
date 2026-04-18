from rest_framework import serializers
from .models import Invite

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ['id',  
                  'athlete', 
                  'sport', 
                  'location', 
                  'start_date', 
                  'end_date', 
                  'start_time', 
                  'end_time', 
                  'message']
    