from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsSuperAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        
        return request.method in SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_staff:
            if request.method in ("GET","PATCH","UPDATE"):
                return True
        return False


