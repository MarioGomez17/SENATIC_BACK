from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRolUsuario

class SerializadorListaRolUsuario(serializers.ModelSerializer):

    def get_Usuario(self,obj):
            return (f"{obj.Usuario.Nombre} "f"{obj.Usuario.Apellido}")

    Rol = serializers.CharField(source="Rol.Nombre")
    Usuario = serializers.SerializerMethodField()

    class Meta:

        model = ModeloRolUsuario

        fields = (
            "Id",
            "Rol",
            "Usuario"
        )