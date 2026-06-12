from rest_framework import serializers

from APLICACION_USUARIOS.models import ModeloRol

class SerializadorCreacionRol(serializers.ModelSerializer):

    class Meta:
        model = ModeloRol

        fields = (
            "Nombre",
        )