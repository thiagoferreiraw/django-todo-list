from rest_framework import generics, viewsets

from .models import Task
from .serializers import TaskSerializer
from .pagination import TaskPagination


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-id")
    serializer_class = TaskSerializer
    max_limit = 50
    pagination_class = TaskPagination
