from rest_framework import serializers
from .models import *

class PrioridadSerializer(serializers.ModelSerializer):
    descripcion = serializers.CharField(required=True)

    class Meta:
        model = AlertaPrioridad
        fields = '__all__'


class EstadoSerializer(serializers.ModelSerializer):
    descripcion = serializers.CharField(required=True)

    class Meta:
        model = AlertaEstado
        fields = '__all__'


class AlertaSerializer(serializers.ModelSerializer):
    prioridad = serializers.PrimaryKeyRelatedField(queryset=AlertaPrioridad.objects.filter(eliminado=False))
    mensaje = serializers.CharField(required=True)
    amenaza = serializers.PrimaryKeyRelatedField(queryset=Amenaza.objects.filter(eliminado=False))
    estado = serializers.PrimaryKeyRelatedField(queryset=AlertaEstado.objects.filter(eliminado=False))

    class Meta:
        model = Alerta
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    alerta = serializers.PrimaryKeyRelatedField(queryset=Amenaza.objects.filter(eliminado=False))
    creador = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.filter(eliminado=False))
    comentario = serializers.CharField(required=True)

    class Meta:
        model = AlertaComentario
        fields = '__all__'

