from rest_framework import serializers

from tasks.models import Task, TaskItem


class TaskItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = ("id", "description", "status")


class TaskSerializer(serializers.ModelSerializer):
    task_items = TaskItemSerializer(many=True)

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        task_items = (
            TaskItem.objects.create(**task_item)
            for task_item in validated_data.pop("task_items")
        )
        task = Task.objects.create(**validated_data)
        task.task_items.add(*task_items)

        return task

    def update(self, instance, validated_data):
        for task_item in validated_data.pop("task_items"):
            print(instance, task_item)
            TaskItem.objects.filter(id=task_item.get("id")).update(**task_item)
        Task.objects.filter(id=instance.id).update(**validated_data)
        instance.refresh_from_db()
        return instance
