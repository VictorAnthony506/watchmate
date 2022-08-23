from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read_only request
            return True
        else:
            # Check permissions for write request
            return bool(request.user and request.user.is_staff)
    
    
class IsReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS is a tuple containing object permissions 'GET', 'OPTIONS', 'HEAD'
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user or request.user.is_staff