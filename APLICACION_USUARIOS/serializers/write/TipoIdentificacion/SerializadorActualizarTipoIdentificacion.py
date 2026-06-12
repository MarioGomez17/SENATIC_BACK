from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloTipoIdentificacion

class SerializadorActualizacionTipoIdentificacion(serializers.ModelSerializer):

    class Meta:
        model = ModeloTipoIdentificacion
        
        fields = (
            "Id",
            "Nombre",
            "Abreviatura",
        )