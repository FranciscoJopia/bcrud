from django.shortcuts import render
from django.http import HttpResponse

# Aqui va la lógica de las vista

# Vista para mostrar dominios a usuarios comunes
def ver_dominios_comunes(request):
    return HttpResponse("Vista de dominios para ususarios comunes")
# Vista para mostrar dominios a ususarios 
def ver_dominios_admin(request):
    return HttpResponse("Vista de dominios para administradores")

def crud_dominios_admin(request):
    return HttpResponse("CRUD de dominios para administradores")

def crud_clientes_admin(request):
    return HttpResponse("CRUD de clientes para administradores")