from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from APLICACION_USUARIOS.models import ModeloUsuario
from APLICACION_USUARIOS.services.ServicioUsuario import ServicioUsuario
from APLICACION_USUARIOS.serializers.read.Usuario import SerializadorListaUsuario, SerializadorDetalleUsuario
from APLICACION_USUARIOS.serializers.write.Usuario import SerializadorCrearUsuario, SerializadorActualizarUsuario

class VistasUsuario(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
    ):

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaUsuario
        if self.action == "retrieve":
            return SerializadorDetalleUsuario
        if self.action == "create":
            return SerializadorCrearUsuario
        if self.action == "update":
            return SerializadorActualizarUsuario

    queryset = ModeloUsuario.objects.all()

    # ===========================================
    # LISTAR (GET /rol/)
    # ===========================================
    def list(self, request):
        Usuarios = ServicioUsuario.ObtenerUsuarios()
        Serializador = SerializadorListaUsuario(Usuarios, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # OBTENER (GET /rol/{id}/)
    # ===========================================
    def retrieve(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        Serializador = SerializadorDetalleUsuario(Usuario)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    # ===========================================
    # CREAR (POST /rol/)
    # ===========================================
    def create(self, request):
        Serializador = SerializadorCrearUsuario(data=request.data)
        Serializador.is_valid(raise_exception=True)
        Roles = Serializador.validated_data.pop("Roles")
        Usuario = ServicioUsuario.CrearUsuario(Serializador.validated_data, Roles)
        SerializadorRespuesta = SerializadorDetalleUsuario(Usuario)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    # ===========================================
    # ACTUALIZAR COMPLETO (PUT /rol/{id}/)
    # ===========================================
    def update(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        Serializador = SerializadorActualizarUsuario(Usuario, data=request.data)
        Serializador.is_valid(raise_exception=True)
        Usuario = ServicioUsuario.ActualizarUsuario(Usuario,Serializador.validated_data)
        return Response(SerializadorDetalleUsuario(Usuario).data, status=status.HTTP_200_OK)

    # ===========================================
    # ACTIVAR (PATCH /rol/{id}/)
    # ===========================================
    def partial_update(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        ServicioUsuario.ActivarUsuario(Usuario)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # ===========================================
    # ELIMINAR (DELETE /rol/{id}/)
    # ===========================================
    def destroy(self, request, pk=None):
        Usuario = ServicioUsuario.ObtenerUsuarioPorId(pk)
        ServicioUsuario.EliminarUsuario(Usuario)
        return Response(status=status.HTTP_204_NO_CONTENT)