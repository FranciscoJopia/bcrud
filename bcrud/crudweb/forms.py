from django import forms
from .models import Dominio, Cliente

# Formulario para administradores (CRUD completo).
class DominioAdminForm(forms.ModelForm):
    class Meta:
        model = Dominio
        fields = ['nombre', 'cliente', 'fecha_creacion', 'fecha_vencimiento','costo_renovacion', 'notas']
        widgets = {
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulario para usuarios comunes (solo lectura).
class DominioUsuarioForm(forms.ModelForm):
    class Meta:
        model = Dominio
        fields = ['nombre', 'fecha_creacion', 'fecha_vencimiento'] # Campo visible para usuarios comunes. 
        widgets = {
            'fecha_creacion': forms.DateTimeInput(attrs={'type': 'datetime-local', 'readonly': 'readonly'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}),
        }
        # Deshabilita toos los campos para que los usuarios no puedan editarlos
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].disable = True

# Formulario para el modelo Cliente (CRUD completo para admin)
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'direccion']