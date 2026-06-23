from rest_framework import status
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from APLICACION_USUARIOS.models import ModeloTipoIdentificacion
from APLICACION_USUARIOS.services.ServicioTipoIdentificacion import ServicioTipoIdentificacion
from APLICACION_USUARIOS.serializers.read.TipoIdentificacion import SerializadorListaTipoIdentificacion, SerializadorDetalleTipoIdentificacion
from APLICACION_USUARIOS.serializers.write.TipoIdentificacion import SerializadorCrearTipoIdentificacion, SerializadorActualizarTipoIdentificacion

class VistasTipoIdentificacion(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
    ):

    def get_serializer_class(self):
        if self.action == "list":
            return SerializadorListaTipoIdentificacion
        if self.action == "retrieve":
            return SerializadorDetalleTipoIdentificacion
        if self.action == "create":
            return SerializadorCrearTipoIdentificacion
        if self.action == "update":
            return SerializadorActualizarTipoIdentificacion    
    
    queryset = ModeloTipoIdentificacion.objects.all()

    #===========================================
    #LISTAR (GET /rol/)
    #===========================================
    def list(self, request):
        TipoIdentificaciones = ServicioTipoIdentificacion.ObtenerTiposIdentificaciones()
        Serializador = SerializadorListaTipoIdentificacion(TipoIdentificaciones, many=True)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    #===========================================
    #OBTENER (GET /rol/{id}/)
    #===========================================
    def retrieve(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        Serializador = SerializadorDetalleTipoIdentificacion(TipoIdentificacion)
        return Response(Serializador.data, status=status.HTTP_200_OK)

    #===========================================
    #CREAR (POST /rol/)
    #===========================================
    def create(self, request):
        Serializador = SerializadorCrearTipoIdentificacion(data=request.data)
        Serializador.is_valid(raise_exception=True)
        TipoIdentificacion = ServicioTipoIdentificacion.CrearTipoIdentificacion(Serializador.validated_data)
        SerializadorRespuesta = SerializadorDetalleTipoIdentificacion(TipoIdentificacion)
        return Response(SerializadorRespuesta.data, status=status.HTTP_201_CREATED)

    #===========================================
    #ACTUALIZAR COMPLETO (PUT /rol/{id}/)
    #===========================================
    def update(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        Serializador = SerializadorActualizarTipoIdentificacion(TipoIdentificacion, data=request.data)
        Serializador.is_valid(raise_exception=True)
        TipoIdentificacion = ServicioTipoIdentificacion.ActualizarTipoIdentificacion(TipoIdentificacion,Serializador.validated_data)
        return Response(SerializadorDetalleTipoIdentificacion(TipoIdentificacion).data, status=status.HTTP_200_OK)

    #===========================================
    #ACTIVAR (PATCH /rol/{id}/)
    #===========================================
    def partial_update(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        ServicioTipoIdentificacion.ActivarTipoIdentificacion(TipoIdentificacion)
        return Response(status=status.HTTP_204_NO_CONTENT)

    #===========================================
    #ELIMINAR (DELETE /rol/{id}/)
    #===========================================
    def destroy(self, request, pk=None):
        TipoIdentificacion = ServicioTipoIdentificacion.ObtenerTipoIdentificacionPorId(pk)
        ServicioTipoIdentificacion.EliminarTipoIdentificacion(TipoIdentificacion)
        return Response(status=status.HTTP_204_NO_CONTENT)