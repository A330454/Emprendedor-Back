from django.db import models

# Create your models here.

#class Relacion(models.Model):
#    nombre_juez= models.ForeignKey()
#    nombre_equipo= models.ForeignKey(Equipo)

class RelacionEquipoJuez(models.Model):
   juez = models.CharField(null=False, blank=False, db_column="juez", max_length=200)
   id_juez = models.PositiveIntegerField(null=False, blank=False, db_column="id_juez")
   equipo = models.CharField(null=False, blank=False, db_column="equipo", max_length=200)
   id_equipo = models.PositiveIntegerField(null=False, blank=False, db_column="id_equipo")
   calificacion=models.FloatField(null=True, blank=True, db_column='calificacion_equipo')
   class Meta:
      db_table='Relacion'
      default_permissions=()
      verbose_name='Informacion de Relacion'
      verbose_name_plural='Informacion de Relaciones'