from rest_framework import serializers
from equipos.models import Equipo, RelacionEquipoJuez
from django.contrib.auth.models import User

class EquipoSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(required=False)
    nombre = serializers.CharField(required=True)
    class Meta:
        model= Equipo
        fields= '__all__'

class EquipoViewSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(required=False)
    class Meta:
        model= Equipo
        fields= ['nombre', 'id','calificacion' ]

# CALIFICACIONES & NOMBRE [PASTEL]

class CalificacionEquipoSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(required=False)
    class Meta:
        model= Equipo
        fields= ['calificacion' ]

class NombreEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Equipo
        fields= ['nombre']

# GANADORES
class GanadoresCalificaiconesEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Equipo
        fields= ['calificacion']

class GanadoresNombreEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Equipo
        fields= ['nombre']

# TABLAS

class TablaEquipoViewSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(required=False)
    class Meta:
        model= Equipo
        fields= ['nombre','calificacion' ]

# RELACION        
class RelacionViewSerializer(serializers.ModelSerializer):
    calificacion = serializers.FloatField(required=False)
    class Meta:
        model= RelacionEquipoJuez
        fields="__all__"

class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model= RelacionEquipoJuez
        fields="__all__"