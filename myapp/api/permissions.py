from rest_framework import permissions


class UserDefinition(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj.owner == request.user) or bool(request.user and request.user.is_staff)