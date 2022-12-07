from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from rest_framework.response import Response

from mixins.serializers import CommonSerializer
from users.serializers import CustomUserSerializer
from .models import Problem, ProblemType, Branch, Author, Source


class ProblemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemType
        fields = ['id', 'title', 'condition']


class BranchSerializer(FlexFieldsModelSerializer):
    # children = RecursiveField(many=True)
    class Meta:
        model = Branch
        fields = '__all__'

    expandable_fields = {
        'parent': ('problems.serializers.BranchSerializer', {'many': False}),
    }


class AuthorSerializer(CommonSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class SourceSerializer(CommonSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class ProblemSerializer(CommonSerializer, FlexFieldsModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'
        expandable_fields = {
            'branch': (BranchSerializer, {'many': False}),
            'problemtype': (ProblemTypeSerializer, {'many': False}),
            'author': (AuthorSerializer, {'many': False}),
            'source': (SourceSerializer, {'many': False}),
            'updated_by': (CustomUserSerializer),
            'created_by': (CustomUserSerializer),
        }


# class RecursiveField(serializers.Serializer):
#     def to_representation(self, value):
#         serializer = self.parent.parent.__class__(value, context=self.context)
#         return serializer.data