from django.db import models
from datetime import datetime

DIA_CHOICE = (
    ("L", "Lunes"),
    ("M", "Martes"),
    ("I", "Miercoles"),
    ("J", "Jueves"),
    ("V", "Viernes"),
    ("S", "Sabado"),
    ("D", "Domingo")
)

class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.IntegerField("Codigo Postal")

    def __str__(self):
        return '%s - CP %s' % (self.nombre,self.cp)

class Persona(models.Model):
    num_doc = models.CharField("Nro Documento", max_length=20, primary_key=True, default=None)
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=150)
    num_cuit = models.CharField("Nro de CUIL/CUIT", max_length=20, null=True, blank=True)
    fecha_nac = models.DateField("Fecha de Nacimiento", default=datetime.now)
    telefono = models.CharField("Nro de Telefono", max_length=50, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    direccion = models.CharField(max_length=120)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name='persona_localidad')

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return '%s - %s' % (self.apellido, self.nombre)

class Profesional(models.Model):
    profesional = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='profesional_persona')
    matricula = models.IntegerField("Matricula", primary_key=True)
    especialidad = models.CharField("Especialidad", max_length=120)

    class Meta:
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return 'Matricula %s - %s' % (self.matricula, self.profesional)

class Calendario(models.Model):
    dia = models.CharField("Dia de la semana", max_length=1, choices=DIA_CHOICE, default='L')
    hora = models.DateTimeField("Hora")

    class Meta:
        ordering = ["dia", "hora"]

    def __str__(self):
        return f'{self.dia}, {self.hora}'

class Usuario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='usuario_persona')
    nombre = models.CharField("Nombre", max_length=20)
    contrasenia = models.CharField("Contraseña", max_length=20)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class ObraSocial(models.Model):
    nombreOS = models.CharField("Nombre Obra Social", max_length=100, primary_key=True)
    direccion = models.CharField("Direccion", max_length=100)
    disponible = models.BooleanField("Disponible")

    class Meta:
        verbose_name_plural = 'ObrasSociales'

    def __str__(self):
        return self.nombreOS

class Turno(models.Model):
    paciente = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='turno_persona')
    medico = models.ForeignKey(Profesional, on_delete=models.PROTECT, related_name='turno_medico')
    fecha = models.ForeignKey(Calendario, on_delete=models.PROTECT, related_name='turno_fecha')
    estado = models.CharField("Estado", max_length=20)

    class Meta:
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return self.paciente

class Paciente(models.Model):
    paciente = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='paciente_persona', default=None)
    numeroHC = models.IntegerField(primary_key=True)
    obraSocial = models.ForeignKey(ObraSocial, on_delete=models.PROTECT, related_name='paciente_obraSocial')
    numOS = models.IntegerField()
    titularFamiliar = models.CharField("Titular Obra Social", max_length=100)

    class Meta:
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return '%s - %d' % (self.paciente, self.numeroHC)

class PiezaDental(models.Model):
    nombre = models.CharField("Nombre Pieza Dental", max_length=100)

    class Meta:
        verbose_name_plural = 'PiezasDentales'

    def __str__(self):
        return self.nombre

class Prestacion(models.Model):
    nombre = models.CharField("Nombre Prestacion", max_length=100)
    descripcion = models.TextField("Descripcion", null=True, blank=True)
    piezaDental = models.ForeignKey(PiezaDental, on_delete=models.PROTECT, related_name='prestacion_piezaDental')

    class Meta:
        verbose_name_plural = 'Prestaciones'

    def __str__(self):
        return self.nombre

class Tratamiento(models.Model):
    medico = models.ForeignKey(Profesional, on_delete=models.PROTECT, related_name='tratamiento_medico')
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name='tratamiento_prestacion')
    fecha = models.ForeignKey(Calendario, on_delete=models.PROTECT, related_name='tratamiento_fecha')
    observacion = models.TextField("Observacion", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Tratamientos'

    def __str__(self):
        return f'{self.prestacion}, {self.fecha}'


class Establecimiento(models.Model):
    nombre = models.CharField("Nombre", max_length=100)
    razonSocial = models.CharField("Razon Social", max_length=100)
    direccion = models.CharField("Direccion", max_length=100)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name='establecimiento_localidad')
    telefono = models.CharField("Nro de Telefono", max_length=50)
    email = models.EmailField("Email", max_length=100)
    web = models.CharField("Web", max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}, {self.direccion}'

class FichaMedica(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.PROTECT, related_name='fichaMedica_establecimiento')
    paciente = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name='fichaMedica_paciente')
    fichaAlta = models.DateField("Ficha Alta", auto_now_add=True)
    tipoFactorSangre = models.CharField("Tipo y Factor de Sangre", max_length=10)
    antecedentes = models.TextField("Antecedentes", null=True, blank=True)
    medicacion = models.CharField("Medicacion", max_length=100)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name='fichaMedica_prestacion')
    historiaClinica = models.ForeignKey(Tratamiento, on_delete=models.PROTECT)

    def __str__(self):
        return self.paciente

class FMedica_Tratamiento(models.Model):
    fichaMedica = models.ForeignKey(FichaMedica, on_delete=models.PROTECT, related_name='fMedica_tratamiento_fichaMedica')
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.PROTECT, related_name='fMedica_tratamiento_tratamiento')

    def __str__(self):
        return f'{self.fichaMedica}, {self.tratamiento}'

class Tratamiento_Prestacion(models.Model):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.PROTECT, related_name='tratamiento_prestacion_tratamiento')
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name='tratamiento_prestacion_prestacion')

    def __str__(self):
        return f'{self.tratamiento}, {self.prestacion}'

class Prestacion_PiezaDental(models.Model):
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name='prestacion_piezaDental_prestacion')
    piezaDental = models.ForeignKey(PiezaDental, on_delete=models.PROTECT, related_name='prestacion_piezaDental_piezaDental')

    def __str__(self):
        return f'{self.prestacion}, {self.piezaDental}'

class Calendario_Turno(models.Model):
    calendario = models.ForeignKey(Calendario, on_delete=models.PROTECT, related_name='calendario_turno_calendario')
    turno = models.ForeignKey(Turno, on_delete=models.PROTECT, related_name='calendario_turno_turno')

    def __str__(self):
        return f'{self.calendario}, {self.turno}'