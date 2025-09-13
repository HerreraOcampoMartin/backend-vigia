import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from common.models.EliminacionLogicaModel import EliminacionLogicaModel
from .repository import CuentaManager


# --- CUENTA ---
# This model should ALWAYS depend on AbstractBaseUser, otherwise, some packages in 'common' app break
class Cuenta(AbstractBaseUser, PermissionsMixin, EliminacionLogicaModel):
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=150, unique=True, blank=False)
    fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_eliminado = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    activo = models.BooleanField(default=True) # TODO: change to false if it's an invitation only software

    # Set the 'objects' property to use the Custom Account Manager
    objects = CuentaManager()

    # TODO: change accordingly
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usuario']

    def __str__(self):
        return f'{self.email} - Usuario: {self.usuario}'


# --- PROFILE ---
class CuentaPerfil(models.Model):
    nombre = models.CharField(max_length=150, blank=False, null=False)
    apellido = models.CharField(max_length=150, blank=False, null=False)
    telefono = models.CharField(max_length=150, blank=True)
    descripcion = models.TextField(max_length=500, blank=True)
    # birthdate
    # country
    # city
    # address
    # gender
    # profile_picture
    # secondary_email
    # alias (how would you like to be called?)
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, verbose_name='usuario', related_name='perfil')

    REQUIRED_FIELDS = ['nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre} + {self.apellido}'


class PasswordResetTokens(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

