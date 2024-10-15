from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    email = models.EmailField(unique=True)
    telefono = PhoneNumberField(     # Usamos PhoneNumberField en lugar de CharField
        unique=True,
        region='CL',
        help_text="Ingresar número fíjo o móvil de forma internacional, Ejemplo:+56XXXXXXXX"
    )
    #telefono = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nombre
# Acá termina el modelo de Cliente
class Dominio(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='dominios', default=1 )   
    # Asumiendo que el cliente con ID 1 es el default 
    # Otra opción es agregar "null=True"
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_vencimiento = models.DateField()
    costo_renovacion = models.IntegerField( 
        default=0, 
        validators=[MinValueValidator(0),           # Valida que el valor sea mayor o igual a 0
                    MaxValueValidator(20000)]       # Valida el valor máximo es 20000    
    )
    #costo_renovacion = models.DecimalField(max_digits=10, decimal_places=0)
    notas = models.TextField(blank=True)                          

    def __str__(self):
        cliente_nombre = self.cliente.nombre if self.cliente else "Sin Cliente" 
        return f"{self.nombre} - {cliente_nombre}"  