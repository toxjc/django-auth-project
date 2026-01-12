from rest_framework import permissions
from .models import UserAssignment, RolePermission

def check_permission(permission_name):
    def has_permission(request, view):
        if not request.user.is_authenticated or not request.user.is_active:
            return False
        try:
            assignments = UserAssignment.objects.filter(user=request.user).select_related('role')
            roles = [a.role for a in assignments]
            perms = RolePermission.objects.filter(role__in=roles).select_related('permission')
            perm_names = [p.permission.name for p in perms]
            return permission_name in perm_names
        except Exception:
            return False
    return has_permission


class HasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Получаем требуемое разрешение из view
        required_perm = getattr(view, 'required_permission', None)
        if not required_perm:
            return True
        return check_permission(required_perm)(request, view)