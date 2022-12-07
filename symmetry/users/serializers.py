from rest_framework import serializers
from .models import userProfile, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class userProfileSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer(read_only=True)
    class Meta:
        model = userProfile
        fields = '__all__'