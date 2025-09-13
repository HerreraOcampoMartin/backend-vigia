from django.contrib.auth.models import BaseUserManager
from django.db import models

class CuentaQuerySet(models.QuerySet):
    def activo(self) -> models.QuerySet:
        return self.filter(activo=True)

    def inactivo(self) -> models.QuerySet:
        return self.filter(activo=False)

    def con_email(self, email: str):
        return self.filter(email=email).first()

    def con_usuario(self, usuario: str):
        return self.filter(usuario=usuario).first()

    def con_id(self, cuenta_id: int):
        return self.filter(id=cuenta_id).first()


class CuentaManager(BaseUserManager):
    """ Accounts manager (repository layer) """
    def get_queryset(self) -> CuentaQuerySet:
        return CuentaQuerySet(self.model, using=self._db)

    def create_user(self, email, usuario, clave, **other_fields):
        if not email:
            raise ValueError('Es necesario proveed un correo')

        email = self.normalize_email(email) # Lower case the domain part of the email.
        user = self.model(email=email, usuario=usuario, **other_fields)
        user.set_password(clave)
        user.save()

        return user

    def create_superuser(self, email: str, usuario: str, clave: str, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('activo', True)

        if not other_fields.get('is_staff'):
            raise ValueError(
                'El superusuario debe ser asignado a is_staff=True')
        if not other_fields.get('is_superuser'):
            raise ValueError(
                'El superusuario debe ser asignado a is_superuser=True')

        return self.create_user(email, usuario, clave, **other_fields)

    def get_by_username(self, usuario: str):
        """ returns Account with provided username or None if not found"""
        return self.get_queryset().con_usuario(usuario)

    def get_by_email(self, email: str):
        """ returns Account with provided email or None if not found"""
        return self.get_queryset().con_email(email)

    def get_by_id(self, cuenta_id: int):
        """ returns Account with provided ID or None if not found"""
        return self.get_queryset().con_id(cuenta_id)



