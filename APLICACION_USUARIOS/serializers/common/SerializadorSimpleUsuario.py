from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.serializers.read.TipoIdentificacion import SerializadorDetalleTipoIdentificacion

class SerializadorSimpleUsuario(serializers.ModelSerializer):

    def get_NombreCompleto(self, obj):
        return f"{obj.Nombre} {obj.Apellido}"

    NombreCompleto = serializers.SerializerMethodField()
    TipoIdentificacion = (SerializadorDetalleTipoIdentificacion())

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
            "Estado",
            "FechaCreacion",
            "FechaActualizacion"
        )