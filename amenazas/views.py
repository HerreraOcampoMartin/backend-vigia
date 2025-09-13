from django_filters.rest_framework import DjangoFilterBackend

from common.permissions import EstaAutenticadoActivo
from common.viewsets import EliminacionLogicaViewSet, PermisosViewSet
from .models import Amenaza, AmenazaCategoria
from .serializers import AmenazaCategoriaSerializer, AmenazaSerializer


class AmenazaViewSet(EliminacionLogicaViewSet, PermisosViewSet):
    """
    Gestionar los endpoints genéricos del modelo Amenaza.
    """
    queryset = Amenaza.objects.all()
    serializer_class = AmenazaSerializer
    filterset_fields = ['id', 'codigoMitre', 'descripcion', "categorias"]
    filter_backends = [DjangoFilterBackend]

    permisos_por_accion = {
        'create': [EstaAutenticadoActivo],
        'update': [EstaAutenticadoActivo],
        'partial_update': [EstaAutenticadoActivo],
        'destroy': [EstaAutenticadoActivo],
        'list': [EstaAutenticadoActivo],
        'retrieve': [EstaAutenticadoActivo],
    }


class AmenazaCategoriaViewSet(EliminacionLogicaViewSet, PermisosViewSet):
    """
    Gestionar los endpoints genéricos del modelo AmenazaCategoria.
    """
    queryset = AmenazaCategoria.objects.all()
    serializer_class = AmenazaCategoriaSerializer
    filterset_fields = ['id', 'descripcion']
    filter_backends = [DjangoFilterBackend]

    permisos_por_accion = {
        'create': [EstaAutenticadoActivo],
        'update': [EstaAutenticadoActivo],
        'partial_update': [EstaAutenticadoActivo],
        'destroy': [EstaAutenticadoActivo],
        'list': [EstaAutenticadoActivo],
        'retrieve': [EstaAutenticadoActivo],
    }



