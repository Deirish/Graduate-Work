# from django.contrib.auth.models import User
# from rest_framework import generics, permissions
# from rest_framework.filters import SearchFilter, OrderingFilter
#
# from myapp.api.serializers import TaskSerializer, TaskCreateSerializer, TaskChangeSerializer
# from myapp.api.permissions import UserDefinition
# from myapp.models import Column
#
#
# class TaskAPIView(generics.ListAPIView):
#     serializer_class = TaskSerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields = ['=status']
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         queryset = Column.objects.all()
#         user = self.request.user
#         if not user.is_superuser:
#             queryset = Column.object.filter(owner=user)
#             return queryset
#         return queryset
#
#
# class TaskCreateAPIView(generics.CreateAPIView):
#     queryset = Column.objects.all()
#     serializer_class = TaskCreateSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class TaskInfoAPIView(generics.RetrieveAPIView):
#     queryset = Column.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated, UserDefinition]
#
#
# class TaskChangeAPIView(generics.RetrieveAPIView):
#     queryset = Column.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated, UserDefinition]
#
#
# class TaskDeleteAPIView(generics.RetrieveDestroyAPIView):
#     queryset = Column.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAdminUser]
#
#
# class TaskChangeAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Column.objects.all()
#     serializer_class = TaskChangeSerializer
#     permission_classes = [permissions.IsAuthenticated]

    # def perform_update(self, serializer):



