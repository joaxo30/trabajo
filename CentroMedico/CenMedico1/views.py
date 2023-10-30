from django.shortcuts import render, redirect
from .forms import PacienteForm 

# Create your views here.

def pagInicio(request):
    return render(request, 'TemplatesCenMedico1/inicio.html')

def pagLogin(request):
    return render(request, 'TemplatesCenMedico1/login.html')

def pagMedico(request):
    return render(request, 'TemplatesCenMedico1/medico.html')
    
def pagTomaDeHora(request):
    return render(request, 'TemplatesCenMedico1/pedirhora.html')
    
def pagRegistro(request):
    if request.method == 'POST':
        paciente_form = PacienteForm(request.POST)
        if paciente_form.is_valid():
            paciente_form.save()
            # Redirige a una página de éxito o donde desees después de guardar en la base de datos
            return redirect('pagina_exito')
    else:
        paciente_form = PacienteForm()

    return render(request, 'TemplatesCenMedico1/registro.html', {'paciente_form': paciente_form})
