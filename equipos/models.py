from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import User

# Create your models here.

class Equipo(models.Model):
   nombre=models.CharField(null=True, blank=True,  max_length=50, db_column='nombre_equipo')
   calificacion=models.FloatField(null=True, blank=True, db_column='calificacion_equipo' )

   def __str__(self) -> str:
      return self.nombre + " " + str(self.pk)

   def actualiza_calificacion(self):
      promedio = 0
      for x in JuecesEquipo.objects.filter(equipo = self):
         promedio += x.calificacion  # type: ignore
      self.calificacion = promedio / JuecesEquipo.objects.filter(equipo = self).count()
   class Meta:
     db_table='Equipos'
     default_permissions=()
     verbose_name='Informacion de Equipo'
     verbose_name_plural='Informacion de Equipos'
class JuecesEquipo(models.Model):
   juez = models.ForeignKey(User, on_delete=models.CASCADE, db_column="juez")
   equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, db_column="equipo")
   calificacion=models.FloatField(null=True, blank=True, db_column='calificacion_equipo' )
   class Meta:
      db_table='Relacion'
      default_permissions=()
      verbose_name='Informacion de Relacion'
      verbose_name_plural='Informacion de Relaciones'