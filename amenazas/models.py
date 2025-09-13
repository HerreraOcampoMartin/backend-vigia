from django.db import models
from common.models import EliminacionLogicaModel


class AmenazaCategoria(EliminacionLogicaModel):
    descripcion = models.CharField(blank=False, null=False, max_length=50)

    REQUIRED_FIELDS = ['descripcion']

    def __str__(self) -> str:
        return f'{self.descripcion}'


class Amenaza(EliminacionLogicaModel):
    codigoMitre = models.CharField(blank=False, null=False, max_length=20)
    categorias = models.ManyToManyField("AmenazaCategoria", related_name="amenazas")
    descripcion = models.CharField(blank=False, null=False, max_length=300)

    REQUIRED_FIELDS = ['codigoMitre', 'categoria', 'descripcion']

    def __str__(self) -> str:
        return f'{self.codigoMitre}: {self.descripcion}'
