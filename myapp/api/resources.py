from django.contrib.auth.models import User
from rest_framework import generics, permissions, exceptions
from rest_framework.filters import SearchFilter, OrderingFilter
from myapp.api.serializers import TaskSerializer, TaskCreateSerializer, TaskChangeSerializer
from myapp.api.permissions import UserDefinition
from myapp.models import Column


class TaskAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['=status']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Column.objects.all()
        user = self.request.user
        if not user.is_superuser:
            queryset = Column.object.filter(owner=user)
            return queryset
        return queryset


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Column.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskInfoAPIView(generics.RetrieveAPIView):
    queryset = Column.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, UserDefinition]


class TaskChangeAPIView(generics.RetrieveAPIView):
    queryset = Column.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, UserDefinition]

    def perform_update(self, serializer):
        obj = self.get_object()
        user = self.request.user
        if 'executor' in serializer.validated_data:
            executor = serializer.validated_data['executor']
            if executor == 'null':
                serializer.save(executor=None)
            else:
                executor_obj = User.objects.get(username=executor)
                if not user.is_superuser:
                    if user == obj.owner == executor_obj:
                        serializer.save(executor=executor_obj)
                    else:
                        message = f"Only ADMIN can choose executor! Enter your name '{user}' or 'null'"
                        raise exceptions.PermissionDenied(message)


class TaskDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Column.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAdminUser]


class TaskStatusChangeAPIView(generics.RetrieveUpdateAPIView):
    queryset = Column.objects.all()
    serializer_class = TaskChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def perform_update(self, serializer):



