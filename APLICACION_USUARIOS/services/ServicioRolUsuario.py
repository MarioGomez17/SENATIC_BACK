from django.db import transaction

from APLICACION_USUARIOS.models import ModeloRolUsuario, ModeloRol

class ServicioRolUsuario:

    @staticmethod
    @transaction.atomic
    def AsignarRoles(Usuario, Roles):
        ModeloRolUsuario.objects.filter(Usuario=Usuario).delete()
        ModeloRolUsuario.objects.bulk_create([ModeloRolUsuario(Usuario=Usuario, Rol=Rol)for Rol in Roles])
        return Usuario

    @staticmethod
    def RemoverRoles(Usuario, Roles):
        ModeloRolUsuario.objects.filter(Usuario=Usuario, rol__in=Roles).delete()