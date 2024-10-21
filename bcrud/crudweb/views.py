from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Dominio, Cliente
from .forms import DominioAdminForm, DominioUsuarioForm, ClienteForm

# Vista para mostrar dominios a usuarios comunes (solo lectura) con búsqueda.
def ver_dominios_comunes(request):
    query = request.GET.get('q')
    if query:
        dominios = Dominio.objects.filter(Q(nombre__icontains=query))
    else:
        dominios = Dominio.objects.all()

    forms = [DominioUsuarioForm(instance=dominio) for dominio in dominios]
    context = {'forms': forms, 'query': query}
    return render(request, 'crudweb/dominios_comunes.html', context)

# Vista para mostrar dominios a administradores (con CRUD) con búsqueda.
def ver_dominios_admin(request):
    query = request.GET.get('q')
    if query:
        dominios = Dominio.objects.filter(Q(nombre__icontains=query) | Q(cliente__nombre__icontains=query))
    else:
        dominios = Dominio.objects.all()

    forms = [DominioAdminForm(instance=dominio) for dominio in dominios]
    context = {'forms': forms, 'query': query}
    return render(request, 'crudweb/dominios_admin.html', context)

# CRUD de dominios para administradores (crear, actualizar, eliminar).
def editar_dominio_admin(request, id=None):
    if id:
        dominio = get_object_or_404(Dominio, id=id)
    else:
        dominio = None

    if request.method == 'POST':
        form = DominioAdminForm(request.POST, instance=dominio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Dominio guardado exitosamente.')
            return redirect('ver_dominios_admin')
        else:
            messages.error(request, 'Error al guardar el dominio. Verifique los datos.')

    else:
        form = DominioAdminForm(instance=dominio)

    context = {'form': form}
    return render(request, 'crudweb/editar_dominios_admin.html', context)

def confirmar_eliminar_dominio(request, dominio_id):
    dominio = get_object_or_404(Dominio, id=dominio_id)
    if request.method == 'POST':
        dominio.delete()
        messages.success(request, 'Dominio eliminado exitosamente.')
        return redirect('ver_dominios_admin')
    return render(request, 'crudweb/confirmar_eliminar_dominio.html', {'dominio': dominio})

# CRUD de clientes para administradores (crear, actualizar, borrar).
def ver_clientes_admin(request):
    query = request.GET.get('q')
    if query:
        clientes = Cliente.objects.filter(Q(nombre__icontains=query))
    else:
        clientes = Cliente.objects.all()

    context = {'clientes': clientes, 'query': query}
    return render(request, 'crudweb/clientes_admin.html', context)

def editar_cliente_admin(request, id=None):
    if id:
        cliente = get_object_or_404(Cliente, id=id)
    else:
        cliente = None

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente guardado exitosamente.')
            return redirect('ver_clientes_admin')
        else:
            messages.error(request, 'Error al guardar el cliente. Verifique los datos.')

    else:
        form = ClienteForm(instance=cliente)

    context = {'form': form}
    return render(request, 'crudweb/editar_cliente_admin.html', context)

def confirmar_eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('ver_clientes_admin')
    return render(request, 'crudweb/confirmar_eliminar_cliente.html', {'cliente': cliente})
