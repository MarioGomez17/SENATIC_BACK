from django.db import models


class ModeloBase(models.Model):

    Estado = models.BooleanField(db_column='Estado', null=False, default=True)
    Fecha_Creacion = models.DateTimeField(db_column='Fecha_Creacion', null=False, auto_now_add=True)
    Fecha_Actualizacion = models.DateTimeField(db_column='Fecha_Actualizacion', null=False, auto_now=True)

    class Meta:
        abstract = True