from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)

from .ModeloBase import ModeloBase
from .ModeloTipoIdentificacion import ModeloTipoIdentificacion
from .UsuarioManager import UsuarioManager

class ModeloUsuario(AbstractBaseUser, PermissionsMixin, ModeloBase):

    Id = models.AutoField(db_column='Id_Usuario', primary_key=True, null=False)
    Nombre = models.CharField(db_column='Nombre_Usuario', max_length=100)
    Apellido = models.CharField(db_column='Apellido_Usuario', max_length=100)
    Telefono = models.CharField(db_column='Telefono_Usuario', max_length=20)
    NumeroIdentificacion = models.CharField(db_column='NumeroIdentificacion_Usuario', max_length=20, unique=True)
    Tipo_Identificacion = models.ForeignKey(ModeloTipoIdentificacion, on_delete=models.PROTECT, db_column='Tipo_Identificacion_Usuario')
    Correo = models.EmailField(db_column='Correo_Usuario', max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "Correo"

    REQUIRED_FIELDS = [
        "Nombre",
        "Apellido",
        "Telefono",
        "NumeroIdentificacion",
        "Tipo_Identificacion"
    ]

    class Meta:
        db_table = "Usuario"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.Nombre

    Objects = UsuarioManager()