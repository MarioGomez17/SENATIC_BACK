from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from APLICACION_USUARIOS.models import ModeloRolUsuario
from APLICACION_USUARIOS.services.ServicioRolUsuario import ServicioRolUsuario
from APLICACION_USUARIOS.serializers.read.RolUsuario import SerializadorListaRolUsuario, SerializadorDetalleRolUsuario

class VistasRolUsuario(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
    ):

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaRolUsuario
        if self.action == "retrieve":
            return SerializadorDetalleRolUsuario

    queryset = ModeloRolUsuario.objects.all()

    #===========================================
    #LISTAR (GET /rol/)
    #===========================================
    def list(self, request):
        RolesUsuarios = ServicioRolUsuario.ObtenerRolesUsuarios()
        Serializador = SerializadorListaRolUsuario(RolesUsuarios, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    #===========================================
    #OBTENER (GET /rol/{id}/)
    #===========================================
    def retrieve(self, request, pk=None):
        RolUsuario = ServicioRolUsuario.ObtenerRolUsuarioPorId(pk)
        Serializador = SerializadorDetalleRolUsuario(RolUsuario)
        return Response(Serializador.data, status=status.HTTP_200_OK)