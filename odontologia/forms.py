from django import forms
from django.forms import ModelForm
from .models import Localidad, Persona, Profesional, Calendario, Usuario, ObraSocial, Turno, Paciente
from .models import PiezaDental, Prestacion, Tratamiento, Establecimiento, FichaMedica, FMedica_Tratamiento
from .models import Tratamiento_Prestacion, Prestacion_PiezaDental, Calendario_Turno

class DateInput(forms.DateInput):
    input_type = 'date'

class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Nombre Localidad'}),
                   'cp': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input'})}

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize', 'placeholder': 'Nombre Paciente'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize'}),
                   'num_doc': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control input'}),
                   'num_cuit': forms.TextInput(attrs= {'type': 'number', 'class': 'form-control input'}),
                   'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class': 'form-control input-sm'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control input'}),
                   'email': forms.TextInput(attrs={'class': 'form-control input'}),
                   'direccion': forms.TextInput(attrs={'class': 'form-control input'}),
                   'localidad': forms.Select(attrs={'class': 'form-control input'})
                   }


class ObraSocialForm(ModelForm):
    class Meta:
        model = ObraSocial
        fields = '__all__'
        widgets = {'nombreOS': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize'}),
                   'direccion': forms.TextInput(attrs= {'class': 'form-control input'}),
                   'disponible': forms.TextInput(attrs={'class': 'form-control input'})
                   }

class PiezaDentalForm(ModelForm):
    class Meta:
        model = PiezaDental
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize'})}

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets ={'persona': forms.Select(attrs={'class': 'form-control input'}),
                  'nombre': forms.TextInput(attrs={'class': 'form-control input'}),
                  'contrasenia': forms.TextInput(attrs={'class': 'form-control input'})
        }

class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {'profesional': forms.Select(attrs={'class': 'form-control input'}),
                   'matricula': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input'}),
                   'especialidad': forms.TextInput(attrs={'class': 'form-control input'})
        }

class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {'paciente': forms.Select(attrs={'class': 'form-control input'}),
                   'medico': forms.Select(attrs={'class': 'form-control input'}),
                   'fecha': DateInput(format='%Y-%m-%d', attrs={'class': 'form-control input-sm'}),
                   # 'estado': forms.TextInput(attrs={'class': 'forms-control input'})
                   }

class PrestacionForm(ModelForm):
    class Meta:
        model = Prestacion
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input'}),
                   'descripcion': forms.TextInput(attrs={'class': 'form-control input'}),
                   'tratamiento': forms.Select(attrs={'class': 'form-control input'})}

class CalendarioForm(ModelForm):
    class Meta:
        model = Calendario
        fields = '__all__'

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'

class EstableciemientoForm(ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'

class FichaMedicaForm(ModelForm):
    class Meta:
        model = FichaMedica
        fields = '__all__'

class FMedica_TratamientoForm(ModelForm):
    class Meta:
        model = FMedica_Tratamiento
        fields = '__all__'

class Tratamiento_PrestacionForm(ModelForm):
    class Meta:
        model = Tratamiento_Prestacion
        fields = '__all__'

class Prestacion_PiezaDentalForm(ModelForm):
    class Meta:
        model = Prestacion_PiezaDental
        fields = '__all__'

class Calendario_TurnoForm(ModelForm):
    class Meta:
        model = Calendario_Turno
        fields = '__all__'