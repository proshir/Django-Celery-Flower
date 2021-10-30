from rest_framework.permissions import BasePermission
class CanUC(BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.groups.filter(name="Gold").exists())