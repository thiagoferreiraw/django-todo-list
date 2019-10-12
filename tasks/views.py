from rest_framework import generics, viewsets

from .models import Task
from .serializers import TaskSerializer

generics.GenericAPIView


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
