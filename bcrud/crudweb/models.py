from django.db import models

# Create your models here.
class Dominio(models.Model):
    nombre = midels.CharField(max_length=100), unique=True)
    frcha_creacion = models.Date