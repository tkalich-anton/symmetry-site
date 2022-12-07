from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

from .models import Definition, Theorem


class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = ['id', 'title', 'body']


class TheoremSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theorem
        fields = ['id', 'title', 'body']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user