from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Athlete
from .serializers import AthleteSerializer
from core.permissions import isParent

# Create your views here.

class AthleteListView(generics.ListCreateAPIView):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        
        queryset = super().get_queryset()
        name = self.request.query_params.get('name')
        surname = self.request.query_params.get('surname')
        sports = self.request.query_params.get('sports')
        location = self.request.query_params.get('location')

        if name:
            queryset = queryset.filter(name__icontains=name)
        
        if surname:
            queryset = queryset.filter(surname__icontains=surname)
        
        if sports:
            queryset = queryset.filter(sports__icontains=sports)
        
        if location:
            queryset = queryset.filter(location__icontains=location)

        return queryset

class AthleteDetailView(generics.RetrieveAPIView):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CreateAthleteView(generics.CreateAPIView):

    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticated, isParent]

    def perform_create(self, serializer):
        
        serializer.save(parent=self.request.user)