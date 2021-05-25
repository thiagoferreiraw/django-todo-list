from django.db import models
from django.db.models.fields.related import ForeignKey


class TaskItem(models.Model):
    description = models.CharField(max_length=250)
    status = models.BooleanField(default=False)


class Task(models.Model):
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    task_items = models.ManyToManyField(TaskItem)

    def __str__(self):
        return self.title
