from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloUsuario

class SerializadorListaUsuario(serializers.ModelSerializer):

    def get_NombreCompleto(self, obj):
        return f"{obj.Nombre} {obj.Apellido}"

    NombreCompleto = (serializers.SerializerMethodField())
    TipoIdentificacion = serializers.CharField(source="TipoIdentificacion.Abreviatura")

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
            "Estado"
        )