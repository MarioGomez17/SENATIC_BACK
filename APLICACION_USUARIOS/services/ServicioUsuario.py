from django.db import transaction
from django.contrib.auth.hashers import make_password

from APLICACION_USUARIOS.models import ModeloUsuario, ModeloRolUsuario, ModeloRol


class ServicioUsuario:

    @staticmethod
    @transaction.atomic
    def crearUsuario(data, Roles):
        """
        Crea usuario + asigna roles
        """
        Usuario = ModeloUsuario.objects.create(
            Nombre=data["Nombre"],
            Apellido=data["Apellido"],
            Correo=data["Correo"],
            Telefono=data["Telefono"],
            NumeroIdentificacion=data["NumeroIdentificacion"],
            TipoIdentificacion=data["TipoIdentificacion"],
            password=make_password(data["password"])
        )
        ModeloRolUsuario.objects.bulk_create([ModeloRolUsuario(Usuario = Usuario, Rol = Rol)for Rol in Roles])
        return Usuario


    @staticmethod
    def obtenerUsuarios():
        return ModeloUsuario.objects.all()
    
    @staticmethod
    def obtenerUsuarioPorId(UsuarioId):
        return ModeloUsuario.objects.get(Id=UsuarioId)
    
    @staticmethod
    @transaction.atomic
    def actualizarUsuario(Usuario, data):
        Usuario.Nombre = data.get("Nombre", Usuario.Nombre)
        Usuario.Apellido = data.get("Apellido", Usuario.Apellido)
        Usuario.Telefono = data.get("Telefono", Usuario.Telefono)
        Usuario.save()
        return Usuario
    
    @staticmethod
    def EliminarUsuario(Usuario):
        Usuario.estado = False
        Usuario.save()
        return Usuario
    
    @staticmethod
    def ActivarUsuario(Usuario):
        Usuario.estado = True
        Usuario.save()
        return Usuario