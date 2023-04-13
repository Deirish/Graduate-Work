from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter

from myapp.api.serializers import ColumnSerializer
from myapp.models import Column


class ColumnAPIView(generics.ListAPIView):
    serializer_class = ColumnSerializer
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


