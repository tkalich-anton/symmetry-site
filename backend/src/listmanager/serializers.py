from rest_framework import serializers

from mixins.serializers import CommonSerializer
from .models import List, Item, MultiItem

from generic_relations.relations import GenericRelatedField

from problems.models import Problem
from academy.models import Definition, Theorem
from problems.serializers import ProblemSerializer
from academy.serializers import DefinitionSerializer, TheoremSerializer


class ListProblemSerializer(CommonSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = List
        fields = ['id', 'status', 'items'] + CommonSerializer.common_fields

    def get_items(self, obj):
        q = Item.objects.filter(list=obj.id)
        serializer = ItemSerializer(q, many=True)
        return serializer.data


class MultiItemSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = MultiItem
        fields = ['id', 'items']

    def get_items(self, obj):
        q = Item.objects.filter(multi_items=obj.id)
        serializer = ItemSerializer(q, many=True)
        return serializer.data


class ItemSerializer(serializers.ModelSerializer):
    content_object = GenericRelatedField({
        Problem: ProblemSerializer(),
        Definition: DefinitionSerializer(),
        Theorem: TheoremSerializer(),
        MultiItem: MultiItemSerializer(),
    })

    class Meta:
        model = Item
        fields = [
            'id',
            'content_type',
            'content_object',
            'item_number',
            'is_active',
            'is_multi_item',
            'is_child',
            'child_number'
        ]