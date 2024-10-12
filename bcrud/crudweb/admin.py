from django.contrib import admin
from .models import Dominio

@admin.register(Dominio)
class DominioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion', 'fecha_vencimiento','costo_renovacion' )
    search_field = ('nombre',)