from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.users.admin.inlines import RolUsuarioInline


@admin.register(ModeloUsuario)
class UsuarioAdmin(UserAdmin):

    ordering = ("Correo",)

    list_display = (
        "Id",
        "Correo",
        "Nombre",
        "Apellido",
        "Telefono",
        "is_staff",
        "is_superuser",
        "Estado"
    )

    search_fields = (
        "Correo",
        "Nombre",
        "Apellido",
        "NumeroIdentificacion"
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "Estado",
        "groups",
    )

    fieldsets = (

        ("Información Personal", {
            "fields": (
                "Correo",
                "password",
                "Nombre",
                "Apellido",
                "Telefono",
                "NumeroIdentificacion",
                "Tipo_Identificacion"
            )
        }),

        ("Permisos", {
            "fields": (
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
                "Estado"
            )
        }),

        ("Fechas", {
            "fields": (
                "last_login",
                "Fecha_Creacion",
                "Fecha_Actualizacion"
            )
        })
    )

    readonly_fields = (
        "Fecha_Creacion",
        "Fecha_Actualizacion",
        "last_login"
    )

    inlines = [
        RolUsuarioInline
    ]
