from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('personas', views.personas_listar, name="personas"),
    path('nueva_persona', views.nueva_persona, name="nueva_persona"),
    path('modificar_persona/<int:pk>', views.modificar_persona, name="modificar_persona"),
    path('eliminar_persona/<int:pk>', views.eliminar_persona, name="eliminar_persona"),
    path('localidades', views.localidades_listar, name="localidades"),
    path('nueva_localidad', views.nueva_localidad, name="nueva_localidad"),
    path('modificar_localidad/<int:pk>', views.modificar_localidad, name="modificar_localidad" ),
    path('eliminar_localidad/<int:pk>', views.eliminar_localidad, name="eliminar_localidad"),
    path('obrasSociales', views.obrasSociales_listar, name="obrasSociales"),
    path('nueva_obraSocial', views.nueva_obraSocial, name="nueva_obraSocial"),
    path('modificar_obraSocial/<str:pk>', views.modificar_obraSocial, name="modificar_obraSocial"),
    path('elimminar_obraSocial/<str:pk>', views.eliminar_obraSocial, name="eliminar_obraSocial"),
    path('usuarios', views.usuario_listar, name="usuarios"),
    path('nuevo_usuario', views.nuevo_usuario, name="nuevo_usuario"),
    path('modificar_usuario/<str:pk>', views.modificar_usuario, name="modificar_usuario"),
    path('eliminar_usuario/<str:pk>', views.eliminar_usuario, name="eliminar_usuario"),
    path('profesionales', views.profesionales_listar, name="profesionales"),
    path('nuevo_profesional', views.nuevo_profesional, name="nuevo_profesional"),
    path('modificar_profesional/<int:pk>', views.modificar_profesional, name="modificar_profesional"),
    path('eliminar_profesional/<int:pk>', views.eliminar_profesional, name="eliminar_profesional"),
    path('piezasDentales', views.piezasDentales_listar, name="piezasDentales"),
    path('nueva_piezaDental', views.nueva_piezaDental, name="nueva_piezaDental"),
    path('modificar_piezaDental/<str:pk>', views.modificar_piezaDental, name="modificar_piezaDental"),
    path('eliminar_piezaDental/<str:pk>', views.eliminar_piezaDental, name="eliminar_piezaDental"),
    path('turnos', views.turnos_listar, name="turnos"),
    path('nuevo_turno', views.nuevo_turno, name="nuevo_turno"),
    path('modificar_turno/<str:pk>', views.modificar_turno, name="modificar_turno"),
    path('eliminar_turno/<str:pk>', views.eliminar_turno, name="eliminar_turno"),
    path('prestaciones', views.prestaciones_listar, name="prestaciones"),
    path('nueva_prestacion', views.nueva_prestacion, name="nueva_prestacion"),
    path('modificar_prestacion/<str:pk>', views.modificar_prestacion, name="modificar_prestacion"),
    path('eliminar_prestacion/<str:pk>', views.eliminar_prestacion, name="eliminar_prestacion")
]
