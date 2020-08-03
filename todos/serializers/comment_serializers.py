from rest_framework import serializers

from todos.models import Comment, Todo


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "todo",
            "text",
            "created_by"
        )

        extra_kwargs = {"created_by": {"write_only": True}}

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        todo_owner = Todo.objects.get(id=data['todo'].id).created_by_id

        if data['created_by'].id != todo_owner:
            raise serializers.ValidationError("Permission denied")
        return data
