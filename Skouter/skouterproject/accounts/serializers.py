import django
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'user_type']

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data['user_type']
        )
        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        
        user = authenticate(username=data['username'],
                             password=data['password'])
        
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        
        token, _ = Token.objects.get_or_create(user=user)
        return {'token': token.key, 'user_id': user.id, 'user_type': user.user_type}
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type']