from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.serializers.common import SerializadorRolResumenUsuario, SerializadorTipoIdentificacionResumen


class SerializadorDetalleUsuario(serializers.ModelSerializer):

    def get_NombreCompleto(self, obj):
        return f"{obj.Nombre} {obj.Apellido}"

    def get_Roles(self, obj):
        return [SerializadorRolResumenUsuario(RolUsuario.Rol).data for RolUsuario in obj.RolesUsuario.all()]

    NombreCompleto = (serializers.SerializerMethodField())
    TipoIdentificacion = SerializadorTipoIdentificacionResumen()
    Roles = serializers.SerializerMethodField()

    class Meta:

        model = ModeloUsuario

        fields = (
            "Id",
            "Nombre",
            "Apellido",
            "NombreCompleto",
            "Correo",
            "Telefono",
            "NumeroIdentificacion",
            "TipoIdentificacion",
            "Roles",
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )