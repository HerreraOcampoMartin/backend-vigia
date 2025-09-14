from rest_framework import permissions

class EsStaff(permissions.BasePermission):
    """
    - Solo permitido para staff
    """

    def has_object_permission(self, request, view, obj):
        usuario = request.user

        if usuario.is_staff:
            return True

        return False
