from django.db import models
from django.utils import timezone
# Create your models here.
class Dominio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateField()
    costo_renovacion = models.DecimalField(max_digits=10, decimal_places=2)
    notas = models.TextField(blank=True)                            