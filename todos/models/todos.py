from django.db import models

from todo_management import settings


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING)

    def __str__(self):
        return self.title
