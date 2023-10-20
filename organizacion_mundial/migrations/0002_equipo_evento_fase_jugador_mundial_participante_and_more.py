# Generated by Django 4.2.4 on 2023-10-19 11:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizacion_mundial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minuto_ocurrido', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nro_pasaporte', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField(default=datetime.date(2005, 1, 1))),
                ('numero_camiseta', models.IntegerField()),
                ('fecha_retiro', models.DateField(blank=True, default=None, null=True)),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizacion_mundial.equipo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mundial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion_obtenida', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('goles_local', models.PositiveSmallIntegerField()),
                ('goles_visitante', models.PositiveSmallIntegerField()),
                ('minutos_ataque', models.PositiveSmallIntegerField()),
                ('cantidad_corners', models.PositiveSmallIntegerField()),
                ('cantidad_laterales', models.PositiveSmallIntegerField()),
                ('fase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion_mundial.fase')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('nro_pasaporte', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateField(default=datetime.date(2005, 1, 1))),
                ('fecha_comienzo', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Posicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_posicion', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='formacion',
            name='defensas',
        ),
        migrations.RemoveField(
            model_name='formacion',
            name='delanteros',
        ),
        migrations.RemoveField(
            model_name='formacion',
            name='mediocampistas',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='abreviatura',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='continente',
        ),
        migrations.RemoveField(
            model_name='pais',
            name='formacion',
        ),
        migrations.AddField(
            model_name='formacion',
            name='esquema',
            field=models.CharField(choices=[('4-4-2', '4-4-2'), ('4-3-3', '4-3-3'), ('3-5-2', '3-5-2'), ('4-2-4', '4-2-4'), ('4-2-3-1', '4-2-3-1'), ('4-3-2-1', '4-3-2-1'), ('3-4-3', '3-4-3')], default='4-4-2', max_length=10),
        ),
        migrations.AddField(
            model_name='pais',
            name='liga_nombre',
            field=models.CharField(default='CORREGI', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Jugadores',
        ),
        migrations.AddField(
            model_name='personal',
            name='pais_perteneciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizacion_mundial.pais'),
        ),
        migrations.AddField(
            model_name='personal',
            name='rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizacion_mundial.rol'),
        ),
        migrations.AddField(
            model_name='partido',
            name='formacion_local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='formacion_local', to='organizacion_mundial.formacion'),
        ),
        migrations.AddField(
            model_name='partido',
            name='formacion_visitante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='formacion_visitante', to='organizacion_mundial.formacion'),
        ),
        migrations.AddField(
            model_name='partido',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pais_local', to='organizacion_mundial.pais'),
        ),
        migrations.AddField(
            model_name='partido',
            name='visitante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pais_visitante', to='organizacion_mundial.pais'),
        ),
        migrations.AddField(
            model_name='participante',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion_mundial.pais'),
        ),
        migrations.AddField(
            model_name='mundial',
            name='pais_sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion_mundial.pais'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion_mundial.pais'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='posicion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizacion_mundial.posicion'),
        ),
        migrations.AddField(
            model_name='fase',
            name='mundial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion_mundial.mundial'),
        ),
        migrations.AddField(
            model_name='evento',
            name='jugador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizacion_mundial.jugador'),
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo_evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizacion_mundial.tipoevento'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='pais_perteneciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizacion_mundial.pais'),
        ),
    ]
