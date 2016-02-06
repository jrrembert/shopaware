from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for all requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions allowed only for owner.
        return obj.created_by == request.user
