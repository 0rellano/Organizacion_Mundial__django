# Generated by Django 4.2.4 on 2023-08-25 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delanteros', models.IntegerField()),
                ('defensas', models.IntegerField()),
                ('mediocampistas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('continente', models.CharField(max_length=20)),
                ('abreviatura', models.CharField(max_length=5)),
                ('formacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizacion_mundial.formacion')),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_camiseta', models.IntegerField()),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizacion_mundial.pais')),
            ],
        ),
    ]
