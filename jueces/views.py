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
    serializer = LoginSerializer(data=data)
    if(serializer.is_valid()):
        return Response(serializer.save(), status=200)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def hola(request):
    return Response("simon", 200)

subjects=[{
    "name":"Brayan",
    "name":"Tadeo",
    "name":"Fer"}]

# API Endpoints
# @csrf_exempt
# def list_subjects(request):
#     if request.method == "GET":
#         return JsonResponse(subjects, safe=False, status=200)
#     if request.method == "POST":
#         juez=request.body
#         print(juez)
#         print(type(juez))
#         juez_data=json.loads(juez)
#         print(juez_data)
#         subjects.append(juez_data)
#         return JsonResponse(juez_data, status=200)

class VacantesServicioViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset=User.objects.all
    serializer_class=serializers.UserSerializer
    renderer_classes=[JSONRenderer]