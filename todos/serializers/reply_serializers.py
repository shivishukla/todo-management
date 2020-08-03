from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from todos.models import Comment, Todo


class ReplySerializer(serializers.ModelSerializer):
    comment_id = PrimaryKeyRelatedField(queryset=Comment.objects.all(), source='parent')

    class Meta:
        model = Comment
        fields = (
            "id",
            "todo",
            'comment_id',
            "text",
            "created_by",
        )

        extra_kwargs = {
            "created_by": {"write_only": True}
        }

    def validate(self, data):

        todo_owner = Todo.objects.get(id=data['todo'].id).created_by_id

        if data['created_by'].id != todo_owner:
            raise serializers.ValidationError("Permission denied")

        comment_owner = Comment.objects.get(id=data['parent'].id).created_by_id

        if data['created_by'].id != comment_owner:
            raise serializers.ValidationError("Permission denied")
        return data
