from django.db import models
from django.contrib.auth.models import User


class Cotizacion(models.Model):
    TIPO_LICITACION = [
        ("Pub", "Público"),
        ("Pri", "Privado"),
    ]

    nombre_proyecto = models.CharField(max_length=200)
    descripcion_proyecto = models.TextField(blank=True)
    fecha_proyecto = models.DateTimeField(null=True)
    cod_licitacion = models.CharField(max_length=50)
    tipo_licitacion = models.CharField(max_length=3, choices=TIPO_LICITACION)
    tipo_construccion = models.CharField(max_length=100)

    precio_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_precio_1 = models.DateTimeField(null=True)

    precio_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_precio_2 = models.DateTimeField(null=True)

    precio_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fecha_precio_3 = models.DateTimeField(null=True)

    enlace = models.URLField(max_length=200)

    usuario_registro = models.ForeignKey(
        User, related_name='cotizaciones_registradas', null=True, on_delete=models.SET_NULL)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    usuario_modifico = models.ForeignKey(
        User, related_name='cotizaciones_modificadas', null=True, on_delete=models.SET_NULL)
    fecha_modifico = models.DateTimeField(null=True)

    def __str__(self):
        return self.nombre_proyecto
