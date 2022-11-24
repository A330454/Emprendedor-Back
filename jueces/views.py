from rest_framework.viewsets import mixins, GenericViewSet
from . import models
from . import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import views
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
@api_view(['POST'])
@permission_classes([])
def login(request):
    data = request.data
    serializer = serializers.LoginSerializer(data=data)
    if(serializer.is_valid()):
        return Response(serializer.save(), status=200)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def hola(request):
    #////////////////////////////////////////////////////////////request.user
    return Response("simon", 200)

# BUSCAR USER BY TOKEN
@api_view(['GET'])
def token_a_user(request):
    response = request.user
    return Response(response, 200)

subjects=[{
    "name":"Brayan",
    "name":"Tadeo",
    "name":"Fer"}]

class VacantesServicioViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset= User.objects.all()
    serializer_class=serializers.UserSerializer

class viewset(GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.filter(is_active = True)
    serializer_class = serializers.UserSerializer

class JuezIndividual(GenericViewSet, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.filter(is_active = True)
    serializer_class = serializers.UserSerializer