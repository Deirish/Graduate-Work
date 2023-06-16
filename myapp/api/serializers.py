from rest_framework import serializers
from django.contrib.auth.models import User
from myapp.models import Column


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display", read_only=True)
    owner = serializers.CharField(default=serializers.CurrentUserDefault(), read_only=True)
    executor = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Column
        fields = ['id', 'owner', 'owner_id', 'status', 'text', 'executor', 'date_update']

    def validate(self, data):
        if 'executor' in data:
            if data['executor'] == 'null':
                return data
            if not User.objects.filter(username=data['executor']).exists():
                raise serializers.ValidationError("No such user exists. Enter another name")
            return data
        else:
            return data


class TaskCreateSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Column
        fields = ['id', 'owner', 'owner_id', 'status', 'text', 'executor', 'date_create']

#
class TaskChangeSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(default=serializers.CurrentUserDefault(), read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    executor = serializers.CharField(read_only=True)

    class Meta:
        model = Column
        fields = ['id', 'owner', 'status', 'executor']
