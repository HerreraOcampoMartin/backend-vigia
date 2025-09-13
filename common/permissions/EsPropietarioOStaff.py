from django.contrib.auth.base_user import AbstractBaseUser
from rest_framework import permissions
from .EstaAutenticadoActivo import EstaAutenticadoActivo

class EsPropietarioOStaff(permissions.BasePermission):
    """
    - Staff puede leer cualquier objeto
    - El dueño puede leer/editar su propio objeto
    """

    def has_permission(self, request, view):
        # Primero, validar que esté autenticado, que esté activado y no sea una cuenta eliminada
        if not EstaAutenticadoActivo().has_permission(request, view):
            return False

        # Permitir al staff todas las acciones
        if request.user.is_staff:
            return True

        return True


    def has_object_permission(self, request, view, obj):
        usuario = request.user

        # Caso genérico: el model tiene una FK a la cuenta
        if hasattr(obj, "cuenta"):
            return obj.cuenta == usuario

        # TODO: es suficiente?
        # Caso especial: el model ES la cuenta
        if isinstance(obj, AbstractBaseUser):
            return obj == usuario

        return False
