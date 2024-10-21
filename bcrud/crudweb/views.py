from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dominio, Cliente
from .forms import DominioAdminForm, DominioUsuarioForm, ClienteForm

# Vista para mostrar dominios a usuarios comunes (solo lectura).
def ver_dominios_comunes(request):
    dominios = Dominio.objects.all()    # Obtén todos los dominios.
    forms = [DominioUsuarioForm(instance=dominio) for dominio in dominios]  # Formularios solo lectura.
    context = {'forms': forms}
    return render(request, 'crudweb/dominios_comunes.html', context)

# Vista para mostrar dominios a administradores (con CRUD).
def ver_dominios_admin(request):
    dominios = Dominio.objects.all()  # Obtén todos los dominios.
    forms = [DominioAdminForm(instance=dominio) for dominio in dominios]  # Formularios pre-rellenados.
    context = {'forms': forms}
    return render(request, 'crudweb/dominios_admin.html', context)

# CRUD de dominios para administradores (crear, actualizar, eliminar).
def editar_dominio_admin(request, id=None):  # Renombrado desde crud_dominios_admin a editar_dominio_admin
    if id:
        dominio = get_object_or_404(Dominio, id=id)
    else:
        dominio = None  # Creación de un nuevo dominio.

    if request.method == 'POST':
        form = DominioAdminForm(request.POST, instance=dominio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dominio guardado exitosamente.')
            return redirect('ver_dominios_admin')  # Redirigir a la lista de dominios.
    else:
        form = DominioAdminForm(instance=dominio)

    context = {'form': form}
    return render(request, 'crudweb/editar_dominios_admin.html', context)  # Actualiza el nombre del template

def confirmar_eliminar_dominio(request, dominio_id):
    dominio = get_object_or_404(Dominio, id=dominio_id)
    if request.method == 'POST':
        dominio.delete()
        messages.success(request, 'Dominio eliminado exitosamente.')
        return redirect('ver_dominios_admin')  # Redirige a la vista que muestra la lista de dominios
    return render(request, 'crudweb/confirmar_eliminar_dominio.html', {'dominio': dominio})  # Muestra la confirmación

# CRUD de cliente para administradores (crear, actualizar, borrar).
def crud_clientes_admin(request, cliente_id=None):
    if cliente_id:  # Si se proporciona un ID, es una actualización o eliminación.
        cliente = get_object_or_404(Cliente, id=cliente_id)
    else:
        cliente = None  # Nuevo cliente.

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente guardado exitosamente.')
            return redirect('crud_clientes_admin')  # Redirige a la vista de clientes admin.
    
    else:
        form = ClienteForm(instance=cliente)

    context = {'form': form}
    return render(request, 'crudweb/crud_clientes_admin.html', context)

