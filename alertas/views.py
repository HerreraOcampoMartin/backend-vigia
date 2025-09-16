from django_filters.rest_framework import DjangoFilterBackend
from common.permissions import EstaAutenticadoActivo, EsStaff, EsPropietarioOStaff
from common.viewsets import PermisosViewSet, EliminacionLogicaViewSet
from .serializers import *


class AlertaPrioridadViewSet(PermisosViewSet):
    queryset = AlertaPrioridad.objects.all()
    serializer_class = PrioridadSerializer
    filterset_fields = ['id', 'descripcion']
    filter_backends = [DjangoFilterBackend]

    permisos_por_accion = {
        'create': [EsStaff],
        'update': [EsStaff],
        'partial_update': [EsStaff],
        'destroy': [EsStaff],
        'list': [EstaAutenticadoActivo],
        'retrieve': [EstaAutenticadoActivo],
    }


class AlertaEstadoViewSet(PermisosViewSet):
    queryset = AlertaEstado.objects.all()
    serializer_class = EstadoSerializer
    filterset_fields = ['id', 'descripcion']
    filter_backends = [DjangoFilterBackend]

    permisos_por_accion = {
        'create': [EsStaff],
        'update': [EsStaff],
        'partial_update': [EsStaff],
        'destroy': [EsStaff],
        'list': [EstaAutenticadoActivo],
        'retrieve': [EstaAutenticadoActivo],
    }


class AlertaViewSet(EliminacionLogicaViewSet, PermisosViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    filterset_fields = ['id', 'prioridad', 'mensaje', 'fecha_hora', 'amenaza', 'estado']
    filter_backends = [DjangoFilterBackend]

    permisos_por_accion = {
        'create': [EstaAutenticadoActivo],
        'update': [EsStaff],
        'partial_update': [EsStaff],
        'destroy': [EsStaff],
        'list': [EstaAutenticadoActivo],
        'retrieve': [EstaAutenticadoActivo],
    }


class AlertaComentarioViewSet(EliminacionLogicaViewSet, PermisosViewSet):
    queryset = AlertaComentario.objects.filter(eliminado=False)
    serializer_class = ComentarioSerializer
    filterset_fields = ['id', 'creador', 'comentario', 'fecha_hora']
    filter_backends = [DjangoFilterBackend]

    permisos_por_accion = {
        'create': [EstaAutenticadoActivo],
        'update': [EsPropietarioOStaff],
        'partial_update': [EsPropietarioOStaff],
        'destroy': [EsPropietarioOStaff],
        'list': [EstaAutenticadoActivo],
        'retrieve': [EstaAutenticadoActivo],
    }

