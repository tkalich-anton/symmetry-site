from rest_framework import serializers


class CommonSerializer(serializers.ModelSerializer):
    """Ensure the fields are included in the models."""

    common_fields = ['created_by', 'created_at', 'updated_by', 'updated_at']