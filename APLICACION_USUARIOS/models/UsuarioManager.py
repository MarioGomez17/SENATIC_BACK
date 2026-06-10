from django.contrib.auth.base_user import BaseUserManager

class UsuarioManager(BaseUserManager):

    def CreateUser(self, Correo, Password=None, **ExtraFields):
        if not Correo:
            raise ValueError("El Correo es obligatorio")
        Correo = self.normalize_email(Correo)
        Usuario = self.model(Correo=Correo, **ExtraFields)
        Usuario.set_Password(Password)
        Usuario.save(using=self._db)
        return Usuario

    def CreateSuperuser(self, Correo, Password, **ExtraFields):
        ExtraFields.setdefault("is_staff", True)
        ExtraFields.setdefault("is_superuser", True)
        return self.CreateUser(Correo, Password, **ExtraFields)
