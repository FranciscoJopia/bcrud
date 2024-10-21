from django.contrib import admin
from .models import Cliente, Dominio

@admin.register(Cliente)                # Registra el modelo Cliente.
class ClienteAdmin(admin.ModelAdmin):   # Puedes Personalizar cómo se verá en el admin.
    list_display = ('nombre', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'email')
    list_filter = ('nombre',)           # Agrega un filtro por nombre de Cliente 

@admin.register(Dominio)
class DominioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cliente', 'fecha_creacion', 'fecha_vencimiento','costo_renovacion' )
    search_fields = ('nombre','cliente__nombre')   # Busca por el nombre del cliente en lugar del ID
    lust_filter = ('fecha_vencimiento', 'cliente') # Filtra dominios por Cliente y fecha de vencimiento 