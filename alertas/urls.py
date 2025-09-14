from rest_framework import routers
from alertas.views import *
from django.urls import path, include

app_name = 'alertas'

router = routers.DefaultRouter()
router.register(r'alertas', AlertaViewSet, basename='alertas')
router.register(r'alertas-estados', AlertaEstadoViewSet, basename='alertas_estados')
router.register(r'alertas-prioridades', AlertaPrioridadViewSet, basename='alertas_prioridades')
router.register(r'alertas-comentarios', AlertaComentarioViewSet, basename='alertas_comentarios')

urlpatterns = [
    path("", include(router.urls)),
]
