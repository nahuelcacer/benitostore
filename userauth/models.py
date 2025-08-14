from django.db import models

# Create your models here.
# quiero agregar datos de envio del usuario
class DatosEnvio(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

    def __str__(self):
        return f"Datos de envío de {self.user.username}"