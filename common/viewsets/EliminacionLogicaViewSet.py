from rest_framework import viewsets

class EliminacionLogicaViewSet(viewsets.ModelViewSet):
    """
    ViewSet abstracto que implementa:
    - Eliminación lógica (en el perform_destroy)
    - Filtra las filas que no fueron eliminadas (eliminado=False)
    """

    # Cada ViewSet tiene que configurar:
    # queryset = Model.objects.filter(eliminado=False)
    # serializer_class = Serializer
    # filterset_fields = [...]

    def get_queryset(self):
        """
        Filtrar solo las filas que no fueron eliminadas (eliminado=False)
        """
        return self.queryset.filter(eliminado=False)
