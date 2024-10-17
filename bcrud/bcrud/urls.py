"""
URL configuration for bcrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Importa el panel de administrador Django.
from django.urls import path
#from . import views
from crudweb import views

urlpatterns = [
    # Rutas de dominios.
    path('dominios/', views.ver_dominios_comunes, name='dominios_comunes'),
    path('admin/dominios/', views.ver_dominios_admin, name='dominios_admin'),
    path('admin/dominios/crud', views.crud_dominios_admin, name='crud_dominios_admin'),

    # Rutas de Clientes (solo admin).
    path('admin/clientes/', views.crud_clientes_admin, name='crud_clientes_admin'),

    # Ruta del panel de administración de Django.
    path('admin/', admin.site.urls),

]