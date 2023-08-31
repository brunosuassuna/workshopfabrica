from rest_framework.viewsets import ModelViewSet

from apps.todo.models import Task
from .serializers import TaskSerializers

class TaskViewSet(ModelViewSet):
    #quero todos os dados que estao na tabela Task    

    queryset = Task.objects.all()

    serializer_class = TaskSerializers