from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to only edit their profile"""

    def has_object_permission(self,request,view,obj):
        """Ensure user is trying to only edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id     