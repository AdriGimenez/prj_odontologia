# Generated by Django 3.2.8 on 2021-10-24 01:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cp', models.IntegerField(verbose_name='Codigo Postal')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('num_doc', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Nro Documento')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre/s')),
                ('apellido', models.CharField(max_length=150)),
                ('num_cuit', models.CharField(blank=True, max_length=20, null=True, verbose_name='Nro de CUIL/CUIT')),
                ('fecha_nac', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de Nacimiento')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nro de Telefono')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('direccion', models.CharField(max_length=120)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='persona_localidad', to='odontologia.localidad')),
            ],
            options={
                'ordering': ['apellido', 'nombre'],
            },
        ),
    ]
