from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser): # general permission

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

class IsAddedByUserOrReadOnly(permissions.BasePermission): #object base permission

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.created_user == request.user or request.user.is_staff
        
class IsAddedByUser(permissions.BasePermission): #object base permission

    def has_object_permission(self, request, view, obj):
        if obj.created_user == request.user and request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff

class IsLoggedInUserOrAdmin(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if obj.user == request.user:
            return True
        return False