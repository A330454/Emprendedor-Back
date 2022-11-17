from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import User


# Create your models here.

class Equipo(models.Model):
   nombre=models.CharField(null=True, blank=True,  max_length=50, db_column='nombre_equipo')
   calificacion=models.FloatField(null=True, blank=True, db_column='calificacion_equipo' )

   def __str__(self) -> str:
      return self.nombre + " " + str(self.pk)

   # def actualiza_calificacion(self):
   #    promedio = 0
   #    for x in JuecesEquipo.objects.filter(equipo = self):
   #       promedio += x.calificacion  # type: ignore
   #    self.calificacion = promedio / JuecesEquipo.objects.filter(equipo = self).count()

   class Meta:
     db_table='Equipos'
     default_permissions=()
     verbose_name='Informacion de Equipo'
     verbose_name_plural='Informacion de Equipos'

# RELACION
class RelacionEquipoJuez(models.Model):
   id_juez = models.PositiveIntegerField(null=False, blank=False, db_column="id_juez")
   id_equipo = models.PositiveIntegerField(null=False, blank=False, db_column="id_equipo")
   calificacion=models.FloatField(null=True, blank=True, db_column='calificacion_equipo')
   nombre_juez=models.CharField(null=False, blank=False, db_column='nombre_juez', max_length=200)
   nombre_equipo=models.CharField(null=False, blank=False, db_column='nombre_equipo', max_length=200)
   class Meta:
      db_table='Asignaciones'
      default_permissions=()
      verbose_name='Informacion de la Relacion'
      verbose_name_plural='Informacion de las Relaciones'
      unique_together = [['id_juez', 'id_equipo']]