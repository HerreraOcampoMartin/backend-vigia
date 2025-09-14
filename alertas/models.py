from django.utils import timezone
from django.db import models
from users.models import Cuenta
from amenazas.models import Amenaza
from common.models import EliminacionLogicaModel


class AlertaPrioridad(EliminacionLogicaModel):
    descripcion = models.TextField(blank=False, null=False)


class AlertaEstado(EliminacionLogicaModel):
    descripcion = models.TextField(blank=False, null=False)


class Alerta(EliminacionLogicaModel):
    prioridad = models.ForeignKey(AlertaPrioridad, on_delete=models.CASCADE)
    mensaje = models.TextField(blank=False, null=False)
    fecha_hora = models.DateTimeField(blank=False, null=False, default=timezone.now)
    amenaza = models.ForeignKey(Amenaza, on_delete=models.CASCADE)
    estado = models.ForeignKey(AlertaEstado, on_delete=models.CASCADE)


class AlertaComentario(EliminacionLogicaModel):
    alerta = models.ForeignKey(Alerta, on_delete=models.CASCADE)
    creador = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    comentario = models.TextField(blank=False, null=False)
    fecha_hora = models.DateTimeField(blank=False, null=False, default=timezone.now)



