from rest_framework import serializers
from amenazas.models import AmenazaCategoria, Amenaza


class AmenazaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Amenaza.
    """
    codigoMitre = serializers.CharField(required=True, min_length=3)
    descripcion = serializers.CharField(required=True, min_length=1)
    categorias = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=AmenazaCategoria.objects.filter(eliminado=False)
    )

    class Meta:
        model = Amenaza
        fields = ['codigoMitre', 'descripcion', 'categorias']


class AmenazaCategoriaSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo AmenazaCategoria.
    """
    descripcion = serializers.CharField(required=True, min_length=4)

    class Meta:
        model = AmenazaCategoria
        fields = '__all__'