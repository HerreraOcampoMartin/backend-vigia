from rest_framework import permissions

class EstaAutenticadoActivo(permissions.BasePermission):
    """
    Grants access only if:
      1 El usuario está a
      2 activo es True
      3 eliminado es False
    """

    def has_permission(self, request, view):
        usuario = request.user
        if not usuario or not usuario.is_authenticated:
            return False

        # Check user fields
        activo = getattr(usuario, "activo", False)
        eliminado = getattr(usuario, "eliminado", False)

        return activo and not eliminado