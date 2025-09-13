import uuid

from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Cuenta, PasswordResetTokens, CuentaPerfil
from .serializers import CuentaSerializer, SoliciarReestablecerClaveSerializer, ReestablecerClaveSerializer, \
    CuentaPerfilSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from common.viewsets import PermisosViewSet, EliminacionLogicaViewSet
from common.permissions import EsPropietarioOStaff, EstaAutenticadoActivo


class CuentaViewSet(EliminacionLogicaViewSet, PermisosViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    filterset_fields = ['id', 'usuario', 'email']
    filter_backends = [DjangoFilterBackend]

    permisos_por_accion = {
        'create': [permissions.AllowAny],
        'update': [EsPropietarioOStaff],
        'partial_update': [EsPropietarioOStaff],
        'destroy': [EsPropietarioOStaff],
        'list': [EstaAutenticadoActivo],
        'retrieve': [EsPropietarioOStaff],
    }


class CuentaPerfilViewSet(PermisosViewSet):
    queryset = CuentaPerfil.objects.all()
    serializer_class = CuentaPerfilSerializer
    filterset_fields = ['nombre', 'apellido', 'telefono']

    permisos_por_accion = {
        'create': [EstaAutenticadoActivo],
        'update': [EsPropietarioOStaff],
        'partial_update': [EsPropietarioOStaff],
        'destroy': [EsPropietarioOStaff],
        'list': [EsPropietarioOStaff],
        'retrieve': [EsPropietarioOStaff],
    }

    lookup_field = "cuenta" # En vez de usar el ID del perfil...

    def get_queryset(self):
        qs = CuentaPerfil.objects.filter(cuenta__eliminado=False)

        return qs

    def perform_destroy(self, instance):
        return Response(
            {"detail": "No se permite eliminar el perfil del usuario. Elimine toda la cuenta"},
            status=status.HTTP_403_FORBIDDEN
        )

    def create(self, request, *args, **kwargs):
        cuenta_id = request.data.get("cuenta")
        if CuentaPerfil.objects.filter(cuenta_id=cuenta_id).exists():
            return Response(
                {"detail": "Esta cuenta ya tiene un perfil."},
                    status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)


class ForgotPasswordController(APIView):
    permission_classes = [AllowAny]

    """
    Handle password reset request. It takes an email and returns a reset link.
    """
    def post(self, request):
        serializador = SoliciarReestablecerClaveSerializer(data=request.data)

        if serializador.is_valid():
            email = serializador.validated_data['email']

            usuario = Cuenta.objects.get_by_email(email)
            if usuario is None:
                return Response({"detail": "No se encontró un usuario con el correo indicado."}, status=status.HTTP_404_NOT_FOUND)

            # Generate a reset token
            reset_token = uuid.uuid4()
            PasswordResetTokens.objects.create(user=usuario, token=reset_token)
            reset_url = f"http://example.com/reset-password/{reset_token}"

            # TODO: send a mail with the full url
            print(f"URL para resetear clave: {reset_url}")

            return Response({"detail": "Un enlace fue enviado a tu correo."},
                            status=status.HTTP_200_OK)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordController(APIView):
    """ Receive new password """
    permission_classes = [AllowAny]
    authentication_classes = ()

    def patch(self, request, tk):
        token = get_object_or_404(PasswordResetTokens, token=tk)
        user = token.cuenta
        serializer = ReestablecerClaveSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            token.delete()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)



class BlacklistTokenController(APIView):
    """ Old tokens go to a blacklist so no one can use them again """
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

