from django.contrib import admin
from users.models import Cuenta
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django.db import models


class UsuarioAdminConfig(UserAdmin):
    model = Cuenta
    search_fields = ('email', 'usuario',)
    list_filter = ('email', 'id', 'usuario', 'eliminado', 'activo', 'is_staff')
    ordering = ('-fecha_creado',)
    list_display = ('email', 'id', 'usuario', 'eliminado', 'activo', 'is_staff')
    fieldsets = (
        # (None, {'fields': ('email', 'usuario',)}),
        ('Permissions', {'fields': ('is_staff', 'eliminado', 'activo', 'is_superuser', 'groups', 'user_permissions')}),
        ('Personal', {'fields': ("usuario",)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'usuario', 'password1', 'password2', 'eliminado', 'activo', 'is_staff')}
         ),
    )


admin.site.register(Cuenta, UsuarioAdminConfig)

