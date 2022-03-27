from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # print(type(request.user), type(obj.email))
        return obj.email == str(request.user)
