# Generated by Django 4.1.3 on 2022-11-16 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, db_column='nombre_equipo', max_length=50, null=True)),
                ('calificacion', models.FloatField(blank=True, db_column='calificacion_equipo', null=True)),
            ],
            options={
                'verbose_name': 'Informacion de Equipo',
                'verbose_name_plural': 'Informacion de Equipos',
                'db_table': 'Equipos',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='RelacionEquipoJuez',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juez', models.CharField(db_column='juez', max_length=200)),
                ('id_juez', models.PositiveIntegerField(db_column='id_juez')),
                ('equipo', models.CharField(db_column='equipo', max_length=200)),
                ('id_equipo', models.PositiveIntegerField(db_column='id_equipo')),
                ('calificacion', models.FloatField(blank=True, db_column='calificacion_equipo', null=True)),
            ],
            options={
                'verbose_name': 'Informacion de la Relacion',
                'verbose_name_plural': 'Informacion de las Relaciones',
                'db_table': 'Asignaciones',
                'default_permissions': (),
            },
        ),
    ]