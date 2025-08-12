from django.db import models
from productos.models import Producto  # Importar el modelo Producto

# Create your models here.

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    

TIPO_MOVIMIENTO = (
    ('entrada', 'Entrada'),
    ('salida', 'Salida'),
    ('ajuste', 'Ajuste')
)

class MovimientoInventario(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo_movimiento.capitalize()} - {self.cantidad} unidades"

    class Meta:
        verbose_name = "Movimiento de Inventario"
        verbose_name_plural = "Movimientos de Inventario"
        ordering = ['-fecha']