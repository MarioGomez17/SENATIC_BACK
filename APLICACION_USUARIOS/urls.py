from rest_framework.routers import DefaultRouter
from .views.VistasRol import VistasRol
from .views.VistasRolUsuario import VistasRolUsuario
from .views.VistasTipoIdentificacion import VistasTipoIdentificacion
from .views.VistasUsuario import VistasUsuario

Router = DefaultRouter()

Router.register("Rol", VistasRol, basename="Rol")
Router.register("RolUsuario", VistasRolUsuario, basename="RolUsuario")
Router.register("TipoIdentificacion", VistasTipoIdentificacion, basename="TipoIdentificacion")
Router.register("Usuario", VistasUsuario, basename="Usuario")

urlpatterns = Router.urls