from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "created_by",
            "title",
            "description",
        )

        def update(self, instance, validated_data):
            validated_data.pop('created_by', None)  # prevent myfield from being updated
            return super().update(instance, validated_data)
