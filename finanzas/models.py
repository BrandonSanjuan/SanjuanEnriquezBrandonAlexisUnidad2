from django.db import models
from django.contrib.auth.models import User


class Movimiento(models.Model):
    TIPOS = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]

    CATEGORIAS = [
        ('comida', 'Comida'),
        ('transporte', 'Transporte'),
        ('escuela', 'Escuela'),
        ('servicios', 'Servicios'),
        ('entretenimiento', 'Entretenimiento'),
        ('salud', 'Salud'),
        ('compras', 'Compras'),
        ('otros', 'Otros'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    fecha = models.DateField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.concepto