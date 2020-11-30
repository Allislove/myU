from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import decorators
from rest_framework.decorators import api_view
from profesores.models import Profesor
from rest_framework import status
from profesores.serializers import ProfesorSerializer


# Create your views here.

@api_view(['GET'])
def profesores(request):
    #Obtengo los datos de los profesores
    profesores = Profesor.objects.all()
    if request.method == 'GET':
        #Si la solicitud es get pues traeme esos datos serializados
        serialized = ProfesorSerializer(profesores, many=True)
        #Retornamos una respuesta positiva si esta se cumple, de lo contrario(else) manda un error
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def profesorId(request):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'DELETE':
        profesor.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({'No se ha podido eliminar el profesor '}, + profesor, + ' ', status=status.HTTP_400_BAD_REQUEST)





