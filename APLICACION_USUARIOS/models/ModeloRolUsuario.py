from django.db import models

from .ModeloBase import ModeloBase
from .ModeloUsuario import ModeloUsuario
from .ModeloRol import ModeloRol

class ModeloRolUsuario(ModeloBase):

    Usuario = models.ForeignKey(ModeloUsuario, on_delete=models.CASCADE, db_column='Usuario_RolUsuario')
    Rol = models.ForeignKey(ModeloRol, on_delete=models.CASCADE, db_column='Rol_RolUsuario')

    class Meta:
        db_table = "Rol_Usuario"
        unique_together = (
            "Usuario",
            "Rol"
        )