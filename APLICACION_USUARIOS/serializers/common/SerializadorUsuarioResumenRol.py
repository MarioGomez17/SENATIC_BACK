from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.serializers.read.TipoIdentificacion import SerializadorDetalleTipoIdentificacion
from APLICACION_USUARIOS.serializers.read.Rol import SerializadorDetalleRol

class SerializadorUsuarioResumenRol(serializers.ModelSerializer):

    def get_NombreCompleto(self, obj):
        return f"{obj.Nombre} {obj.Apellido}"

    NombreCompleto = serializers.SerializerMethodField()
    TipoIdentificacion = serializers.CharField(source="TipoIdentificacion.Abreviatura")

    class Meta:

        model = ModeloUsuario

        fields = (
            "Id",
            "NombreCompleto",
            "NumeroIdentificacion",
            "TipoIdentificacion"
        )