from django.shortcuts import render, redirect, get_object_or_404
try:
    # Prefer absolute imports first (helps linters and editors)
    from clinica.models import Paciente, Medico, Cita
    from clinica.forms import PacienteForm, MedicoForm, CitaForm
except (ImportError, ModuleNotFoundError):
    # Fallback to relative imports when running as a package
    from .models import Paciente, Medico, Cita # type: ignore
    from .forms import PacienteForm, MedicoForm, CitaForm # type: ignore

# CRUD PACIENTES
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/lista.html', {'pacientes': pacientes})

def crear_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'paciente/form.html', {'form': form, 'accion': 'Crear'})

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('lista_pacientes')
    return render(request, 'paciente/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect('lista_pacientes')


# CRUD MÉDICOS
def lista_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/lista.html', {'medicos': medicos})

def crear_medico(request):
    form = MedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_medicos')
    return render(request, 'medico/form.html', {'form': form, 'accion': 'Crear'})

def editar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    form = MedicoForm(request.POST or None, instance=medico)
    if form.is_valid():
        form.save()
        return redirect('lista_medicos')
    return render(request, 'medico/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_medico(request, id):
    medico = get_object_or_404(Medico, id=id)
    medico.delete()
    return redirect('lista_medicos')


# CRUD CITAS
def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'cita/lista.html', {'citas': citas})

def crear_cita(request):
    form = CitaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_citas')
    return render(request, 'cita/form.html', {'form': form, 'accion': 'Crear'})

def editar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    form = CitaForm(request.POST or None, instance=cita)
    if form.is_valid():
        form.save()
        return redirect('lista_citas')
    return render(request, 'cita/form.html', {'form': form, 'accion': 'Editar'})

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    cita.delete()
    return redirect('lista_citas')
