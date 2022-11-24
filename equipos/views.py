from django.shortcuts import render
from equipos.models import Equipo
from rest_framework.response import Response
from rest_framework.views import APIView
from equipos.serializers import EquipoSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import mixins, GenericViewSet
from . import models
from . import serializers
from rest_framework.renderers import JSONRenderer
from equipos.serializers import EquipoViewSerializer
from equipos.serializers import RelacionViewSerializer, PruebaSerializer

# POR EVALUACIÓN

class EquiposSinEvaluarViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset=models.Equipo.objects.filter(calificacion=None)
    serializer_class=serializers.EquipoSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

class EquiposEvaluadosViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=models.Equipo.objects.exclude(calificacion=None)
    serializer_class=serializers.EquipoSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

# TODOS

class TodosLosEquiposViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=models.Equipo.objects.all()
    serializer_class=serializers.EquipoViewSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

class TodosLosEquiposNombresViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=models.Equipo.objects.all().exclude(calificacion=None)
    serializer_class=serializers.NombreEquipoSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

class TodosLosEquiposCalificacionesViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=models.Equipo.objects.all().exclude(calificacion=None)
    serializer_class=serializers.CalificacionEquipoSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

# ELIMINAR TODOS
class EliminarEquiposViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset=models.Equipo.objects.all()
    serializer_class=serializers.EquipoViewSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

    @api_view(['DELETE'])
    def delete_all(request):
        models.Equipo.objects.all().delete()
        return Response(status=204)

# GANADORES

class EquiposGanadoresViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset=models.Equipo.objects.order_by('-calificacion')[:10]
    serializer_class=serializers.EquipoSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

class CalificacionEquiposGanadoresViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset=models.Equipo.objects.order_by('-calificacion')[:10]
    serializer_class=serializers.GanadoresCalificaiconesEquipoSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

class NombreEquiposGanadoresViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset=models.Equipo.objects.order_by('-calificacion')[:10]
    serializer_class=serializers.GanadoresNombreEquipoSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

# TABLAS
class TablaAdminEquiposGanadoresViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset=models.Equipo.objects.all()
    serializer_class=serializers.TablaEquipoViewSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

# RELACIÓN
class RelacionViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset=models.RelacionEquipoJuez.objects.all()
    serializer_class=serializers.RelacionViewSerializer
    renderer_classes=[JSONRenderer]
    permission_classes = []

# CONTAR RELACIONES CON CALIFICACION
#class RelacionCountNotNullViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
#    queryset=models.RelacionEquipoJuez.objects.all().exclude(calificacion=None)
#    serializer_class=serializers.RelacionViewSerializer
#    renderer_classes=[JSONRenderer]
#    permission_classes = []

    # def retrieve(self, request, *args, **kwargs):
    #     calificaiones = models.RelacionEquipoJuez.objects.filter('')
    #     return super().retrieve(request, *args, **kwargs)

# RELACIONES NO EVALUADAS
@api_view(['GET'])
@permission_classes([])
def get_relacion_by_juez(request, id):
    relaciones = models.RelacionEquipoJuez.objects.filter(id_juez=id)
    print(relaciones)
    data_serializador = PruebaSerializer(relaciones, many=True)
    #response = [data_serializador]
    return Response(data_serializador.data, status=200)

# RELACIONES NO EVALUADAS POR JUEZ
@api_view(['GET'])
@permission_classes([])
def get_relacion_null_by_juez(request, id):
    relaciones = models.RelacionEquipoJuez.objects.filter(id_juez=id, calificacion=None)
    print(relaciones)
    data_serializador = PruebaSerializer(relaciones, many=True)
    #response = [data_serializador]
    return Response(data_serializador.data, status=200)

@api_view(['GET'])
@permission_classes([])
def get_relacion_by_equipo(request, id):
    if request.method == "GET":
        relaciones = models.RelacionEquipoJuez.objects.filter(id_equipo=id)
        print(relaciones)
        data_serializador = PruebaSerializer(relaciones, many=True)
        #response = [data_serializador]
        return Response(data_serializador.data, status=200)
    if request.method == "PATCH":
        pass
    else:
        return Response("method not allowed", 405)

# COUNT
@api_view(['GET'])
@permission_classes([])
def cuenta_relacionones_calificadas_by_equipo(request, id):
    if request.method == "GET":
        relaciones = models.RelacionEquipoJuez.objects.filter(id_equipo=id).exclude(calificacion=None).count()
        print(relaciones)
        data_serializador = PruebaSerializer(relaciones)
        #response = [data_serializador]
        return Response(relaciones, status=200)
    if request.method == "PATCH":
        pass
    else:
        return Response("method not allowed", 405)


@api_view(['GET'])
@permission_classes([])
def relacionones_calificadas_by_equipo(request, id):
    if request.method == "GET":
        relaciones = models.RelacionEquipoJuez.objects.filter(id_equipo=id).exclude(calificacion=None)
        print(relaciones)
        data_serializador = PruebaSerializer(relaciones, many=True)
        #response = [data_serializador]
        return Response(data_serializador.data, status=200)
    if request.method == "PATCH":
        pass
    else:
        return Response("method not allowed", 405)


@api_view(['GET'])
@permission_classes([])
def get_1_relacion(request, id):
    relaciones = models.RelacionEquipoJuez.objects.filter(id)
    print(relaciones)
    data_serializador = PruebaSerializer(relaciones, many=True)
    #response = [data_serializador]
    return Response(data_serializador.data, status=200)

@api_view(['GET'])
@permission_classes([])
def graficaPastel1(request):
    equipos_evualuados = models.Equipo.objects.filter(calificacion=None).count()
    equipos_no_evualuados = models.Equipo.objects.all().exclude(calificacion=None).count()
    response = [equipos_evualuados,equipos_no_evualuados]
    return Response(data = response, status=200)



#@api_view(['GET'])
#@permission_classes([])
#def eliminar_todos_los_equipos(request):
#    todos_los_equipos = models.Equipo.objects.all().delete()
#    data_serializador = EquipoSerializer(todos_los_equipos)
#    return Response(data_serializador, status=200)


#@api_view(['GET'])
#@permission_classes([])
#def get_cal_equip(request, equipo):
#    try:
#        equipo = models.Equipo.objects.get(pk=equipo)
#    except:
#        pass ##quipo no exixte, no fue encontradp
#
#    equipo.actualiza_calificacion()
#    return(equipo.calificacion, 200)