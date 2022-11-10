from email.policy import default
from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict


# Create your models here.

class Equipo(models.Model):
   nombre=models.CharField(null=True, blank=True,  max_length=50, db_column='nombre_equipo')
   calificacion=models.FloatField(null=True, blank=True, db_column='calificacion_equipo' )

   def __str__(self) -> str:
      return self.nombre+ " " + str(self.pk)

   class Meta:
     db_table='Equipos'
     default_permissions=()
     verbose_name='Informacion de Equipo'
     verbose_name_plural='Informacion de Equipos'
