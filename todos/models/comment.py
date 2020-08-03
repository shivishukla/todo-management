from django.db import models

from todos.models import Todo
from todo_management import settings


class Comment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)
    created_date = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return self.text
