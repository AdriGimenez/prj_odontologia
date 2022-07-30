from django.shortcuts import render, redirect
from .models import Persona, Localidad, ObraSocial, Usuario, Profesional, Turno, PiezaDental, Prestacion
from .forms import PersonaForm, LocalidadForm, ObraSocialForm, UsuarioForm, ProfesionalForm, TurnoForm, PiezaDentalForm, PrestacionForm

def index(request, template_name='odontologia/index.html'):
    return render(request, template_name)

def personas_listar(request, template_name='odontologia/personas.html'):
    personas = Persona.objects.all()
    dato_personas = {"personas": personas}
    return render(request, template_name, dato_personas)

def nueva_persona(request, template_name='odontologia/persona_form.html'):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('personas')
    else:
        form = PersonaForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def modificar_persona(request, pk, template_name='odontologia/persona_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_persona(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    persona = Persona.objects.get(num_doc=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('personas')
    else:
        return render(request, template_name)

def nueva_localidad(request, template_name='odontologia/localidad_form.html'):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
    else:
        form = LocalidadForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def localidades_listar(request, template_name='odontologia/localidades.html'):
    localidades = Localidad.objects.all()
    dato_localidades = {"localidades": localidades}
    return render(request, template_name, dato_localidades)

def modificar_localidad(request, pk, template_name='odontologia/localidad_form.html'):
    localidad = Localidad.objects.get(id=pk)
    form = LocalidadForm(request.POST or None, instance=localidad)
    if form.is_valid():
        form.save(commit=True)
        return redirect('localidades')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_localidad(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    localidad = Localidad.objects.get(id=pk)
    if request.method == 'POST':
        localidad.delete()
        return redirect('localidades')
    else:
        return render(request, template_name)

def nueva_obraSocial(request, template_name='odontologia/obraSocial_form.html'):
    if request.method == 'POST':
        form = ObraSocialForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('obrasSociales')
    else:
        form = ObraSocialForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def obrasSociales_listar(request, template_name='odontologia/obrasSociales.html'):
    obrasSociales = ObraSocial.objects.all()
    dato_obrasSociales = {"obrasSociales": obrasSociales}
    return render(request, template_name, dato_obrasSociales)

def modificar_obraSocial(request, pk, template_name='odontologia/obraSocial_form.html'):
    obraSocial = ObraSocial.objects.get(nombreOS=pk)
    form = ObraSocialForm(request.POST or None, instance=obraSocial)
    if form.is_valid():
        form.save(commit=True)
        return redirect('obrasSociales')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_obraSocial(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    obraSocial = ObraSocial.objects.get(nombreOS=pk)
    if request.method == 'POST':
        obraSocial.delete()
        return redirect('obrasSociales')
    else:
        return render(request, template_name)

def nuevo_usuario(request, template_name='odontologia/usuario_form.html'):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def usuario_listar(request, template_name='odontologia/usuarios.html'):
    usuarios = Usuario.objects.all()
    dato_usuarios = {"usuarios": usuarios}
    return render(request, template_name, dato_usuarios)

def modificar_usuario(request, pk, template_name='odontologia/usuario_form.html'):
    usuario = Usuario.objects.get(nombre=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save(commit=True)
        return redirect('usuarios')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_usuario(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    usuario = Usuario.objects.get(nombre=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')
    else:
        return render(request, template_name)

def nuevo_profesional(request, template_name='odontologia/profesional_form.html'):
    if request.method == "POST":
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profesionales')
    else:
        form = ProfesionalForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def profesionales_listar(request, template_name='odontologia/profesionales.html'):
    profesionales = Profesional.objects.all()
    dato_profesionales = {"profesionales": profesionales}
    return render(request, template_name, dato_profesionales)

def modificar_profesional(request, pk, template_name='odontologia/profesional_form.html'):
    profesional = Profesional.objects.get(matricula=pk)
    form = ProfesionalForm(request.POST or None, instance=profesional)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profesionales')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_profesional(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    profesional = Profesional.objects.get(matricula=pk)
    if request.method == 'POST':
        profesional.delete()
        return redirect('profesionales')
    else:
        return render(request, template_name)

def nuevo_turno(request, template_name='odontologia/turno_form.html'):
    if request.method == "POST":
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('turnos')
    else:
        form = TurnoForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def turnos_listar(request, template_name='odontologia/turnos.html'):
    turnos = Turno.objects.all()
    dato_turnos = {"turnos": turnos}
    return render(request, template_name, dato_turnos)

def modificar_turno(request, pk, template_name='odontologia/turno_form.html'):
    turno = Turno.objects.get(paciente=pk)
    form = TurnoForm(request.POST or None, instance=turno)
    if form.is_valid():
        form.save(commit=True)
        return redirect('turnos')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_turno(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    turno = Turno.objects.get(paciente=pk)
    if request.method == 'POST':
        turno.delete()
        return redirect('turnos')
    else:
        return render(request, template_name)

def nueva_piezaDental(request, template_name='odontologia/piezaDental_form.html'):
    if request.method == "POST":
        form = PiezaDentalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('piezasDentales')
    else:
        form = PiezaDentalForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def piezasDentales_listar(request, template_name='odontologia/piezasDentales.html'):
    piezasDentales = PiezaDental.objects.all()
    dato_piezasDentales = {"piezasDentales": piezasDentales}
    return render(request, template_name, dato_piezasDentales)

def modificar_piezaDental(request, pk, template_name='odontologia/piezaDental_form.html'):
    piezaDental = PiezaDental.objects.get(nombre=pk)
    form = PiezaDentalForm(request.POST or None, instance=piezaDental)
    if form.is_valid():
        form.save(commit=True)
        return redirect('piezasDentales')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_piezaDental(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    piezaDental = PiezaDental.objects.get(nombre=pk)
    if request.method == 'POST':
        piezaDental.delete()
        return redirect('piezasDentales')
    else:
        return render(request, template_name)

def nueva_prestacion(request, template_name='odontologia/prestacion_form.html'):
    if request.method == "POST":
        form = PrestacionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('prestaciones')
    else:
        form = PiezaDentalForm()
    dato = {"form": form}
    return render(request, template_name, dato)

def prestaciones_listar(request, template_name='odontologia/prestaciones.html'):
    prestaciones = Prestacion.objects.all()
    dato_prestaciones = {"prestaciones": prestaciones}
    return render(request, template_name, dato_prestaciones)

def modificar_prestacion(request, pk, template_name='odontologia/prestacion_form.html'):
    prestacion = Prestacion.objects.get(nombre=pk)
    form = PrestacionForm(request.POST or None, instance=prestacion)
    if form.is_valid():
        form.save(commit=True)
        return redirect('prestaciones')
    else:
        print(form.errors)
    datos = {"form": form}
    return render(request, template_name, datos)

def eliminar_prestacion(request, pk, template_name='odontologia/confirmar_eliminacion.html'):
    prestacion = Prestacion.objects.get(nombreOS=pk)
    if request.method == 'POST':
        prestacion.delete()
        return redirect('prestaciones')
    else:
        return render(request, template_name)
