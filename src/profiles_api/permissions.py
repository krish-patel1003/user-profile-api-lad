from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to eddit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            """Allows users to view data but not edit"""
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """Allows users to update thier own status"""

    def has_object_permission(self, request, view, obj):
        """Checks the user is trying to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user.id == request.user.id