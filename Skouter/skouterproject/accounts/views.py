from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(generics.GenericAPIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

class ProfileView(APIView):
    
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)
