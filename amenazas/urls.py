from django.urls import path, include
from rest_framework.routers import DefaultRouter
from amenazas.views import AmenazaViewSet, AmenazaCategoriaViewSet

app_name = "amenazas"

router = DefaultRouter()
router.register(r"amenazas", AmenazaViewSet, basename="amenazas")
router.register(r"amenazas/categorias", AmenazaCategoriaViewSet, basename="categorias")

urlpatterns = [
    path("", include(router.urls)),
]
