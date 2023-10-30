from django import forms
from .models import Roles, Usuario, Paciente, Consulta_medica, Informe

class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ('cod_rol', 'nombre')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('rut', 'nombre', 'email', 'telefono', 'cod_rol')

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('rut', 'nombre', 'telefono', 'direccion', 'contrasena', 'confirmar_contrasena')

class ConsultaMedicaForm(forms.ModelForm):
    class Meta:
        model = Consulta_medica
        fields = ('cod_consulta', 'rut_usuario', 'rut_paciente')
        widgets = {
            'fecha': forms.SelectDateWidget(),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

class InformeForm(forms.ModelForm):
    class Meta:
        model = Informe
        fields = ('cod_informe', 'cod_consulta')

