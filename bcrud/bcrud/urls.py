from django.contrib import admin
from django.urls import path
from crudweb import views

urlpatterns = [
    # Rutas de dominios
    path('dominios/', views.ver_dominios_comunes, name='dominios_comunes'),  # Vista para usuarios comunes
    path('admin/dominios/', views.ver_dominios_admin, name='ver_dominios_admin'),  # Vista para administradores
    path('admin/dominios/crear/', views.editar_dominio_admin, name='crear_dominio_admin'),  # Crear un nuevo dominio
    path('admin/dominios/editar/<int:id>/', views.editar_dominio_admin, name='editar_dominio_admin'),  # Editar un dominio existente
    path('admin/dominios/eliminar/<int:dominio_id>/', views.confirmar_eliminar_dominio, name='eliminar_dominio_admin'),  # Confirmar eliminación de un dominio

    # Rutas de Clientes (solo admin)
    path('admin/clientes/', views.crud_clientes_admin, name='crud_clientes_admin'),  # CRUD de clientes

    # Ruta del panel de administración de Django
    path('admin/', admin.site.urls),
]


