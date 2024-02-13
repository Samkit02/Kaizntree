from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
    security_question = serializers.CharField(max_length=255)
    security_answer = serializers.CharField(max_length=255)

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value


class ForgotPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    security_question = serializers.CharField(max_length=255)
    security_answer = serializers.CharField(max_length=255)
