from rest_framework import viewsets

class PermisosViewSet(viewsets.ModelViewSet):
    """
    Base ViewSet for managing permissions per action.
    """
    permisos_por_accion = {}

    # How to define the permissions in the child classes:
    # permission_classes_by_action = {
    #     'create': [permissions.AllowAny],
    #     'update': [IsOwner],
    #     'partial_update': [IsOwner],
    #     'destroy': [IsOwner],
    #     'list': [permissions.IsAuthenticated],
    #     'retrieve': [permissions.IsAuthenticated],
    # }

    def get_permissions(self):
        """
        Returns the corresponding permissions of the current action.
        If not defined, use permission_classes, which is the default in Django Rest Framework.
        """
        try:
            permission_classes = self.permisos_por_accion[self.action]
        except KeyError:
            permission_classes = self.permission_classes  # fallback a default
        return [p() for p in permission_classes]
