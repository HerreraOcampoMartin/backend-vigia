from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = "usuarios"

router = DefaultRouter()
router.register(r'cuentas', CuentaViewSet, basename='cuenta')
router.register(r'perfiles', CuentaPerfilViewSet, basename='perfil')

urlpatterns = [
    path('', include(router.urls)),
    path("olvido-clave/", ForgotPasswordController.as_view(), name="olvido_clave"),
    path("reestablecer-clave/<str:tk>/", ResetPasswordController.as_view(), name="reestablecer_clave"),
]