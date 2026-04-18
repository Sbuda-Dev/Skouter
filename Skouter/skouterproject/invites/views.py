from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Invite
from .serializers import InviteSerializer
from scouts.models import ScoutProfile

# Create your views here.

class CreateInviteView(generics.CreateAPIView):

    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        
        scout_profile = ScoutProfile.objects.get(user=self.request.user)
        serializer.save(scout=scout_profile)

class RespondInviteView(generics.UpdateAPIView):

    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):

        invite = self.get_object()
        user = self.request.user

        if invite.athlete.parent != user:
            raise permissions.PermissionDenied("You do not have permission to respond to this invite.")
        
        status = self.request.data.get('status')

        if status not in ['accepted', 'declined']:
            raise permissions.ValidationError("Invalid status. Must be 'accepted' or 'declined'.")
        
        serializer.save(status=status)